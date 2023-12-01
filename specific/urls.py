from specific.views import *

from django.urls import path

app_name='something'

urlpatterns=[
    
    path('lalitha/',lalitha,name='lalitha'),
    path('vasundhara/',vasundhara,name='vasundhara'),
]