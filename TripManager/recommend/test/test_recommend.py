from .test_setup import TestSetUp
from account.models import User
class TestViews(TestSetUp):
    def test_post_recommendation(self):
        data = {'query': 'lake'}
        response = self.client.post(self.recommend_url, data, format='json')
        self.assertEqual(response.status_code, 201)


    




 