from django.http import response
from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIClient

class EndpointTests(TestCase):
    def test_predict_view(self):
        client = APIClient()
        input_data = [
            {
                "raceID": 1,
                "horseID": 1,
                "weight": 100,
                "ageInDays": 1000,
                "daysSinceLastRace": 10,
                "nPastRaces": 10 
            },
            {
                "raceID": 1,
                "horseID": 2,
                "weight": 200,
                "ageInDays": 5000,
                "daysSinceLastRace": 1000,
                "nPastRaces": 1
            }
        ]
        classifier_url = '/api/v1/predict_race_winners/predict'
        response = client.post(classifier_url, input_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['raceID'], 1)
        self.assertEqual(response.data['horseID'], 1)
        self.assertTrue('request_id' in response.data)
        self.assertTrue('status in response.data')