from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # check if content return is application/json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/login')
        self.assertEqual(response.content_type, 'application/json')

    # check data returned
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get('/login')
        self.assertTrue(b'msg' in response.data)

    # Ensure that login behaves correctly given the correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(email="chalindu.18@cse.mrt.ac.lk", password="Password"),
            follow_redirects=True
        )
        # self.assertEqual("msg", response.data)


if __name__ == '__main__':
    unittest.main()