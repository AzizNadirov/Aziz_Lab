from django.contrib import admin
from django.urls import path

from apps.main.views import HomePageView
from apps.transformer.views import Transformer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name = "home_page"),
    path('transformer/', Transformer.as_view(), name = "transformer"),
]
