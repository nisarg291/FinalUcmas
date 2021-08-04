"""ucmas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
# from users import views as user_views
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
admin.site.site_header = "Parth Academy UCMAS SYSTEM"
admin.site.site_title = "Parth Academy UCMAS SYSTEM"
admin.site.index_header = "Parth Academy UCMAS SYSTEM"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', user_views.profile,name="profile"),
    # path('accounts/',include('allauth.urls')),
    path("",include('webapp.urls')),
    path("user/",include('users.urls')),
    path('edit/', user_views.edit, name='edit'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/',user_views.login_view,name='login'),
    path('islogin', user_views.islogin),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path("password-reset/", PasswordResetView.as_view(template_name='password_reset.html'),name="password_reset"),

	path("password-reset/done/", PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),

	path("password-reset-confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),

    path("password-reset-complete/", PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),
   # path('verification/', include('verify_email.urls'),name="verification"),
    # path('resendOTP', resend_otp),
    #path('verification/', include('verify_email.urls'),name="verification"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)