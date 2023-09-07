from .test_setup import TestSetUp
from account.models import User
from django.core.exceptions import PermissionDenied  # Import PermissionDenied
class TestViews(TestSetUp):
    def test_post_posts(self):
        data = {'body': 'Good place to visit'}
        response = self.client.post(self.posts_url, data, format='json')
        self.assertEqual(response.status_code, 201)
    def test_user_cannot_post_with_no_data(self):
        res=self.client.post(self.posts_url)
        import pdb
        pdb.set_trace()
        self.assertEqual(res.status_code,400) 


    




 