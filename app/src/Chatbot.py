from numpy.lib.twodim_base import tri
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import random
from tensorflow.python.framework import ops
import pickle
import json

with open('intents.json') as file:
    data = json.load(file)



words = []
labels = []
docs_x = []
docs_y = []

#####################################################################
####Data for model. Inputs for input layer
#####################################################################

with open("data.pickle", "rb") as f: #rb = read bytes
    words, labels, training, output = pickle.load(f)

# for intent in data['intents']:
#     for pattern in intent['patterns']:
#         wrds = nltk.word_tokenize(pattern) #Give a list with all of the different words. Nltk has a function for this
#         words.extend(wrds)
#         docs_x.append(wrds)
#         docs_y.append(intent["tag"])
        
#     if intent['tag'] not in labels:
#         labels.append(intent['tag']) # all the tags added
        
# #Remove ? marks. Because people may type those. we ignore them
# words = [stemmer.stem(w.lower()) for w in words if w != "?"] #all words are in lower case and take root words
# words = sorted(list(set(words))) #Remove duplicates using set

# labels = sorted(labels)
# #Right now we have lists of strings. Neural network only understands numbers
# #So we create bag of words that they represent all of the words in any given pattern. We will use that to train our model.
# #Bag of words is whats know as one hot encoded which means that  
# #If our words are "a", "bite", "goodbye" -> [0,1,2] we find frequency of words into a list
# #It is called one hot encoded, because it just represents like if the word is there or not.
# #This is a really good input to our neural network. so we can essentially just determine what
# #words are there and what words are not there. Neural network cant compute if the inputs are strings

# #Data preprocessing to make the model
# training = [] #list of 0s and 1s. 1 hot encoded
# output = [] #list of 0s and 1s

# #output list with 0s
# out_empty = [0 for _ in range(len(labels))] 
# # if out_empty = [0, 0, 0, 1], "shop","greetings", "goodbye", "name". Name is the intent

# #create bag of words
# for x, doc in enumerate(docs_x):
#     bag = [] #one hot encoded bag of words 
#     wrds = [stemmer.stem(w) for w in doc] #stem words in doc_x
    
    
#     for w in words:
#         if w in wrds: #the word exist in current pattern we are looping through
#             bag.append(1) #if the word exist, we append 1
#         else:
#             bag.append(0)
#     output_row = out_empty[:]
#     output_row[labels.index(docs_y[x])] = 1 
    
#     training.append(bag)
#     output.append(output_row)

# #Turn these into Numpy arrays. Because we have to work with numpy arrays in tflearn
# training = numpy.array(training)
# output = numpy.array(output)

# #Save data on a file
# with open("data.pickle", "wb") as f: #wb = wrtie byte
#     pickle.dump((words, labels, training, output), f)


#Make the model
#We are gonn build our model using tflearn. This is very similar to tensorflow

#####################################################################
####TFLearn model creation. This is the complete AI part here
#####################################################################
ops.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8) 
net = tflearn.fully_connected(net, len(output[0]), activation="softmax") 
net = tflearn.regression(net)

model = tflearn.DNN(net) 
####################################
#####################################################################
####Save Neural Network
#####################################################################
# try:
#     
# except:
    #e_epoch - number of times the model, sees the training data set
model.load("model.tflearn")
# model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
# model.save("model.tflearn")


#####################################################################
####Turn input sentences into bag of words according one hot encoding
#####################################################################
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))] 

    s_words = nltk.word_tokenize(s) 
    s_words = [stemmer.stem(word.lower()) for word in s_words] 

    for se in s_words:
        for i, w in enumerate(words):
            if w == se: 
                bag[i] = 1

    return numpy.array(bag)

def chat(inp):
    # print("Hello, I am Xyron. I'm an expert in telecommunication domain")
    # while True:
    #     inp = input("You: ")
    #     if inp.lower() == "quit":
    #         break
           
    #make predictions
    results = model.predict([bag_of_words(inp, words)])[0] 
    results_index = numpy.argmax(results) 
    tag = labels[results_index]

    res = ""
    if results[results_index] > 0.7:
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        res = random.choice(responses)
    else:
        res = "I didn't get that"
    
    return res


# def chat(inp):
#     # print("Start talking with bot")
#     # while True:
#     #     inp = input("You: ")
#     #     if inp.lower() == "quit":
#     #         break

#     results = model.predict([bag_of_words(inp, words)])
#     results_index = numpy.argmax(results)
#     tag = labels[results_index]
#     # if tag == "predict":
#     #     return "predict"
#     # else:
#     res = ""
#     for tg in data["intents"]:
#         if tg["tag"] == tag:
#             responses = tg["responses"]
#             print(responses)
#             res = random.choice(responses)
#     return res