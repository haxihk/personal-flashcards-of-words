document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("reset-password-form");

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        const email = document.getElementById("email").value;

        if (!email) {
            alert("لطفاً ایمیل خود را وارد کنید.");
        } else {
            alert(`لینک بازیابی رمز عبور به ایمیل ${email} ارسال شد.`);
        }
    });
});
