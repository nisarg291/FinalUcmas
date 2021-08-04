from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .views import resend_otp,notifications,clear_notifications,login_view,islogin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
# from users import views as user_views
from . import views
urlpatterns = [
    path("password-reset/", PasswordResetView.as_view(template_name='password_reset.html'),name="password_reset"),
    path('login/', login_view, name = 'login'),
	path("password-reset/done/", PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('islogin', islogin),
	path("password-reset-confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),

	path("password-reset-complete/", PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),
    path('verification/', include('verify_email.urls'),name="verification"),
    path('resendOTP', resend_otp),
    path('notifications', notifications),
	path('notifications/clear', clear_notifications),
	
	
	
]