import json

try:
    from run import app
    import unittest

except Exception as e:
    print(("Some Modules are missig {}".format(e)))


class Telecom_test(unittest.TestCase):
    greeting = ['Hello!, How can I help you ?', 'Good to see you again!, How can I help you ?',
                'Hi there,  How can I help you ?', 'Hello!, How can I help you ?']

    Q1 = ["package"]
    Q2 = ["balance"]
    Q3 = ["complaint"]
    AI = ["Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think.", "AI is the field of science which concerns itself with building hardware and software that replicates the functions of the human mind."]
    creator = ["Chalindu, Sandaruwan & Geeth are my creators", "I am owned by a group in University of Moratuwa", "My owners are studying at UoM"]

    def test_1_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)  # check API call work properly
        self.assertEqual(response.content_type, "application/json")  # check the return content is application/json
        self.assertTrue(b'"members":["Member","Hello Sandaruwan"]' in response.data)  # check correct data is returned

    def test_2_reply(self):
        tester = app.test_client(self)
        # calling backend API
        response_greaating = tester.post("/reply", json={'msg': 'hi'})
        response_predict = tester.post("/reply", json={'msg': "I'm not feeling well"})
        response_channel = tester.post("/reply", json={'msg': "schedule an appointment"})
        response_todayCovid = tester.post("/reply", json={'msg': "today covid-19 deaths in sri lanka"})
        response_currentCovid = tester.post("/reply", json={'msg': "how about current covid situation in sri lanka"})
        response_globalCovid = tester.post("/reply", json={'msg': "current world covid-19 situation"})
        response_clinic = tester.post("/reply", json={'msg': "do you have any clinic details"})
        response_thank = tester.post("/reply", json={'msg': "thanks your help"})

        status_code = response_greaating.status_code
        self.assertEqual(status_code, 200)  # check API call work properly

        self.assertEqual(response_greaating.content_type,
                         "application/json")  # check the return content is application/json

        # response data for each backend request
        data_greeting = json.loads(response_greaating.data)
        data_predict = json.loads(response_predict.data)
        data_channel = json.loads(response_channel.data)
        data_todayCovid = json.loads(response_todayCovid.data)
        data_currentCovid = json.loads(response_currentCovid.data)
        data_globalCovid = json.loads(response_globalCovid.data)
        data_clinic = json.loads(response_clinic.data)
        data_thank = json.loads(response_thank.data)

        self.assertTrue(data_greeting['members'] in Telecom_test.greeting)
        self.assertTrue(data_predict['members'] in Telecom_test.predict)
        self.assertTrue(data_channel['members'] in Telecom_test.channel)
        self.assertTrue(data_todayCovid['members'] in Telecom_test.todayCovid)
        self.assertTrue(data_currentCovid['members'] in Telecom_test.currentCovid)
        self.assertTrue(data_globalCovid['members'] in Telecom_test.globalCovid)
        self.assertTrue(data_clinic['members'] in Telecom_test.clinic)
        self.assertTrue(data_thank['members'] in Telecom_test.thank)

    def test_3_getPackageTypes(self):
        tester = app.test_client(self)
        response = tester.post("/getPackageTypes")
        status_code = response.status_code
        self.assertEqual(status_code, 200)  # check API call work properly
        self.assertEqual(response.content_type, "application/json")  # check the return content is application/json
        data = json.loads(response.data)
        self.assertEqual(data['disease'], "Fungal infection")  # check correct data is returned

    def test_4_getPackages(self):
        tester = app.test_client(self)
        response = tester.post("/getPackages")
        status_code = response.status_code
        self.assertEqual(status_code, 500)  # check API call work properly
        self.assertEqual(response.content_type, "application/json")  # check the return content is application/json
        data = json.loads(response.data)
        self.assertEqual(len(data)>0)  # check correct data is returned

    def test_5_getPackageInformation(self):
        tester = app.test_client(self)
        response = tester.post("/getPackageInformation")
        status_code = response.status_code
        self.assertEqual(status_code, 500)  # check API call work properly

    def test_6_sendfeedbak(self):
        tester = app.test_client(self)
        response = tester.post("/sendFeedback", json={"specialist": 'acupuncture'})
        status_code = response.status_code
        self.assertEqual(status_code, 500)  # check API call work properly

if __name__ == "__main__":
    unittest.main()
