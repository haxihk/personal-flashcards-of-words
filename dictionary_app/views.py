from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import WordForm
from .models import Word
from django.contrib import messages


# ویوی ثبت‌نام
def register_view(request):
    if request.user.is_authenticated:  # اگر کاربر لاگین کرده باشد
        return redirect('home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ورود خودکار پس از ثبت‌نام
            messages.success(request, 'ثبت‌نام با موفقیت انجام شد.')
            return redirect('home')  # آدرس صفحه اصلی (home) را تنظیم کنید
        else:
            messages.error(request, 'خطا در ثبت‌نام. لطفاً اطلاعات را بررسی کنید.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# ویوی ورود
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'با موفقیت وارد شدید.')
            return redirect('home')  # آدرس صفحه اصلی (home) را تنظیم کنید
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

# ویوی خروج
def logout_view(request):
    logout(request)
    messages.info(request, 'شما خارج شدید.')
    return redirect('login')  # آدرس صفحه ورود را تنظیم کنید

def manage_words_view(request):
    # نمایش و مدیریت کلمات
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            definition = form.cleaned_data['definition']
            language = form.cleaned_data['language']

            # بررسی وجود کلمه در پایگاه داده
            existing_word = Word.objects.filter(word=word).first()
            if existing_word:
                existing_word.definition = definition  # به‌روزرسانی معنی
                existing_word.language = language      # به‌روزرسانی زبان
                existing_word.save()
                messages.success(request, f'کلمه "{word}" با موفقیت به‌روزرسانی شد.')
            else:
                # افزودن کلمه جدید
                Word.objects.create(word=word, definition=definition, language=language)
                messages.success(request, f'کلمه "{word}" با موفقیت اضافه شد.')

            return redirect('manage_words')  # بازگشت به صفحه مدیریت کلمات

    else:
        form = WordForm()

    # لیست کلمات برای نمایش
    words = Word.objects.all()
    return render(request, 'manage.html', {'form': form, 'words': words})
