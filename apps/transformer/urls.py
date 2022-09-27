from django.urls import path

from .views import Transformer, Transforming, Analysing



urlpatterns = [
    path('', Transformer.as_view(), name='transformer'),
    path('ting/', Transforming.as_view(), name='ting'),
    path('aing/', Analysing.as_view(), name='aing'),
]