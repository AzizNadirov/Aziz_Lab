from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from apps.main.views import HomePageView
from apps.transformer.views import Transformer
import debug_toolbar



urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name="home_page"),
    path('transformer/', include('apps.transformer.urls'), name="transformer"),
    path('register/', include('apps.account.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name="logout"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
