#from django.contrib import admin
#from django.urls import path, include
#urlpatterns = [
   # path('admin/', admin.site.urls),
   # path("", include("ablog.urls")),
#]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
path('admin/', admin.site.urls),
path('', include('theblog'.urls)),
path('members/', include('django.contrib.auth.urls')),
path('members/', include('members.urls')),
path('register/', UserRegisterView.as_view(), name='register'),
path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
path('password/', auth_views.PasswordChangeView.as_view(template_name='register')),
path('password/', PasswordsChangeView.as_view(template_name='registration/change')),
path('password_success', name="password_success"),
path('<int:pk>/profile/', ShowProfilePageView.as_view(),  name='show_profile_page'),
path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(),  name='edit_profile_page'),
path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
