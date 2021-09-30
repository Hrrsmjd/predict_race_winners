from django.urls import path

from apps.frontend.views import Index
from apps.frontend.views import HowTo
from apps.frontend.views import Predict

# router 

urlpatterns = [
    path('', Index, name='index'),
    path('howto/', HowTo, name='howto'),
    path('predict/', Predict, name='predict')
]