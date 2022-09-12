from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from apps.main.views import HomePageView
from apps.base.views import LikeView, SaveView, SupportView
import debug_toolbar
from apps.account import views as users_views

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls')),
    path('register/', include('apps.account.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name="logout"),
    path('user/<str:username>/', users_views.user, name='user'),
    path('profile/', users_views.ProfileView.as_view(), name='profile'),
    path('edit/', users_views.edit_profile_view, name='edit_profile'),
    path('blog/', include('apps.blog.urls')),
    path('apps/transformer/', include('apps.transformer.urls'), name="transformer"),
    path('qs/', include('apps.forum.urls')),
    path('treasure/', users_views.TreasureListView.as_view(), name="my_treasure"),
    path('like', LikeView.as_view(), name="like"),
    path('support', SupportView.as_view(), name="support"),
    path('save', SaveView.as_view(), name="save"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
