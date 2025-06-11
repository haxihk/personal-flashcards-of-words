from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # مسیر صفحه ورود
    path('register/', views.register_view, name='register'),  # مسیر صفحه ثبت‌نام
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='dictionary_app/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='dictionary_app/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='dictionary_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='dictionary_app/password_reset_complete.html'), name='password_reset_complete'),
]
