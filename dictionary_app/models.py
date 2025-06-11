from django.contrib.auth.models import AbstractUser
from django.db import models

# مدل کاربر (در صورت نیاز به افزودن فیلدهای اضافی)
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # ایمیل به‌عنوان فیلد یکتا
    REQUIRED_FIELDS = ['email']  # ایمیل در هنگام ثبت‌نام اجباری می‌شود

class Word(models.Model):
    ENGLISH = 'EN'
    PERSIAN = 'FA'
    LANGUAGE_CHOICES = [
        (ENGLISH, 'English'),
        (PERSIAN, 'Persian'),
    ]

    word = models.CharField(max_length=100, unique=True)  # کلمه
    definition = models.TextField()  # معنی کلمه
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)  # زبان کلمه
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ آخرین به‌روزرسانی

    def __str__(self):
        return self.word

# مدل ثبت فعالیت کاربران
class UserActivityLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # کاربر
    action = models.CharField(max_length=100)  # نوع فعالیت
    timestamp = models.DateTimeField(auto_now_add=True)  # زمان فعالیت

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"
