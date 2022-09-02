from django.urls import path

from apps.transformer.views import Transformer

urlpatterns = [
    path('apps/transformer', Transformer.as_view(), name = "transformer"),
]