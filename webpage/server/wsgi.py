"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()

# ML registry 
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.predict_race_winners.logistic_regression import LogisticRegression

try:
    # Create ML registry
    registry = MLRegistry()
    # Logistic regression
    log_reg = LogisticRegression()
    # Add to ML registry
    registry.add_algorithm(endpoint_name='predict_race_winners',
                           algorithm_object=log_reg,
                           algorithm_name = 'Logistic regression',
                           algorithm_status = 'Production',
                           algorithm_version = '0.0.1',
                           owner = 'Harris',
                           algorithm_description = 'Logistic regression with simple pre- and post-processing',
                           algorithm_code = inspect.getsource(LogisticRegression)  
                        ) 
except Exception as e: 
    print('Exception while loading the algorithms to the registry,', str(e))