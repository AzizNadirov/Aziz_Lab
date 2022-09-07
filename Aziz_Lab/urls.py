from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.main.views import HomePageView
from apps.transformer.views import Transformer
import debug_toolbar



urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name = "home_page"),
    path('transformer/', include('apps.transformer.urls'), name = "transformer"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
