from .test_setup import TestSetUp
from account.models import User
class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        res=self.client.post(self.register_url)
         # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code,400) 
    
    def test_user_can_register_correctly(self):
        res=self.client.post(
            self.register_url,self.user_data,format="json")
        # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code,201)

    def test_user_cannot_register_with_different_passowrd(self):
        self.user_data['confirm_password'] = 'differentpassword'
        res=self.client.post(
            self.register_url,self.user_data,format="json")
        # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code,400)
    def test_user_cannot_register_with_same_passowrd(self):
        self.user_data['confirm_password'] = 'hello1234567'
        res=self.client.post(
            self.register_url,self.user_data,format="json")
        # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code,201)
    
    def test_user_can_login_no_data(self):
        res=self.client.post(
            self.login_url)
         # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code,400)
    
    def test_user_can_login_correctly(self):
    # Create a user with known login credentials
        user = User.objects.create_user(
            username="Prabin",
            email="prabin@gmail.com",
            password="hello1234567",
        )

    # Use the correct email and password for the login attempt
        login_data = {
            "email": "prabin@gmail.com",
            "password": "hello1234567",
        }
        res = self.client.post(self.login_url, login_data, format="json")
         # import pdb
        # pdb.set_trace()
        # Check that the response status code is 200 (OK) for a successful login
        self.assertEqual(res.status_code, 200)



    




 