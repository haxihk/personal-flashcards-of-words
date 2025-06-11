document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("signup-form");
    const captchaContainer = document.getElementById("captchaCode");
    const captchaInput = document.getElementById("captchaInput");

    // ایجاد کپچا
    function generateCaptcha() {
        const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        const length = 6;
        let captcha = "";
        for (let i = 0; i < length; i++) {
            captcha += chars.charAt(Math.floor(Math.random() * chars.length));
        }
        captchaContainer.textContent = captcha;
    }

    // بررسی کپچا هنگام ارسال فرم
    form.addEventListener("submit", (event) => {
        event.preventDefault();
        const userCaptcha = captchaInput.value;
        const generatedCaptcha = captchaContainer.textContent;

        if (userCaptcha === generatedCaptcha) {
            alert("ثبت‌نام با موفقیت انجام شد!");
            close("signup.html");
            open("login.html");
            
        } else {
            alert("کپچا اشتباه است. لطفاً دوباره تلاش کنید.");
            generateCaptcha(); // تولید مجدد کپچا
        }
    });

    // تولید کپچا در زمان بارگذاری صفحه
    generateCaptcha();
});
