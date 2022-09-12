from django.urls import path, include

from apps.transformer.views import Transformer

urlpatterns = [
    path('', include('apps.main.urls'), name="home"),
]