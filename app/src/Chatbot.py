from app import routes
from app import db

import nltk
from nltk.stem.lancaster import LancasterStemmer

import numpy
import tflearn
from tensorflow.python.framework import ops
import random
import json
#load pickle data
import pickle
nltk.download('punkt')
stemmer = LancasterStemmer()

with open("intents.json") as file:
    data = json.load(file)

words = [] #all the words in intents
labels = [] #all the tags
#Each words in doc x corresponding to an entry doc y
docs_x = []
docs_y = []

#####################################################################
####Data for model. Inputs for input layer
#####################################################################

try:
    with open("data.pickle", "rb") as f: #rb = read bytes
        words, labels, training, output = pickle.load(f)
except:
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern) #Give a list with all of the different words. Nltk has a function for this
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"]) # all the tags added

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    #Remove ? marks. Because people may type those. we ignore them
    words = [stemmer.stem(w.lower()) for w in words if w not in "?"] #all words are in lower case and take root words
    words = sorted(list(set(words))) #Remove duplicates using set
    labels = sorted(labels) 

#Right now we have lists of strings. Neural network only understands numbers
#So we create bag of words that they represent all of the words in any given pattern. We will use that to train our model.
#Bag of words is whats know as one hot encoded which means that  
#If our words are "a", "bite", "goodbye" -> [0,1,2] we find frequency of words into a list
#It is called one hot encoded, because it just represents like if the word is there or not.
#This is a really good input to our neural network. so we can essentially just determine what
#words are there and what words are not there. Neural network cant compute if the inputs are strings
    
    #Data preprocessing to make the model
    training = [] #list of 0s and 1s. 1 hot encoded
    output = [] #list of 0s and 1s

    #output list with 0s
    out_empty = [0 for _ in range(len(labels))]

    # if out_empty = [0, 0, 0, 1], "shop","greetings", "goodbye", "name". Name is the intent
    
    #create bag of words
    for x, doc in enumerate(docs_x):
        bag = [] #one hot encoded bag of words 
        wrds = [stemmer.stem(w) for w in doc] #stem words in doc_x

        for w in words:
            if w in wrds: #the word exist in current pattern we are looping through
                bag.append(1) #if the word exist, we append 1
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    #Turn these into Numpy arrays. Because we have to work with numpy arrays in tflearn
    training = numpy.array(training)
    output = numpy.array(output)

    #Save data on a file
    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)


#Make the model
#We are gonn build our model using tflearn. This is very similar to tensorflow

#####################################################################
####TFLearn model creation. This is the complete AI part here
#####################################################################
ops.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])]) #Input layer
net = tflearn.fully_connected(net, 8) #1st hidden layer with 8 neurons
net = tflearn.fully_connected(net, 8) #2nd hidden layer with 8 neurons
net = tflearn.fully_connected(net, len(output[0]), activation="softmax") #Output layer with number of neurons equal to the number of tags
#Softmax allows us to get probability for each output. Softmax gives a probability for each neuron
net = tflearn.regression(net)

model = tflearn.DNN(net)

# model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
# model.save("model.tflearn")


model.load("model.tflearn")


#####################################################################
####Turn input sentences into bag of words according one hot encoding
#####################################################################
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))] # words in intents
    s_words = nltk.word_tokenize(s) #input sentence word list
    s_words = [stemmer.stem(word.lower()) for word in s_words] #stemming all the words

    for se in s_words:
        for i, w in enumerate(words):
            if w == se: #current word of inputs is in word list
                bag[i] = 1

    return numpy.array(bag)


def chat(inp):
    #make predictions
    results = model.predict([bag_of_words(inp, words)])[0]
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    if results[results_index] > 0.7:
        for tg in data["intents"]:
            if tg["tag"] == tag:
                responses = tg["responses"]
                print(responses)
                res = random.choice(responses)
    else:
        res = "I didn't understand it"
    return res