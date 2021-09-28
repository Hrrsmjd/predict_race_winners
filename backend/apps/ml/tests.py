import inspect

from django.http import response
from django.test import TestCase

from apps.ml.predict_race_winners.logistic_regression import LogisticRegression
from apps.ml.registry import MLRegistry


class MLTests(TestCase):
    def test_log_reg(self):
        input_data = [
            {
                'raceID': 1,
                'horseID': 1,
                'weight': 100,
                'ageInDays': 1000,
                'daysSinceLastRace': 10,
                'nPastRaces': 10 
            },
            {
                'raceID': 1,
                'horseID': 2,
                'weight': 200,
                'ageInDays': 5000,
                'daysSinceLastRace': 1000,
                'nPastRaces': 1
            }
        ]
        my_alg = LogisticRegression()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('raceID' in response)
        self.assertTrue('horseID' in response)


    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = 'predict_race_winners'
        algorithm_object = LogisticRegression()
        algorithm_name = 'Logistic regression'
        algorithm_status = 'Production'
        algorithm_version = '0.0.1'
        algorithm_owner = 'Harris'
        algorithm_description = 'Logistic regression with simple pre- and post-processing'
        algorithm_code = inspect.getsource(LogisticRegression)
        # Add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # There should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)