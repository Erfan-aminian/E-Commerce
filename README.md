# 🛒 E-Commerce Platform (Django)

یک فروشگاه اینترنتی ساده و قابل توسعه با استفاده از **Django**. این پروژه شامل امکانات پایه یک سیستم فروشگاه آنلاین از جمله ثبت‌نام کاربران، نمایش محصولات، افزودن به سبد خرید، پرداخت و مدیریت سفارش‌ها می‌باشد.

## 📌 ویژگی‌ها

- ثبت‌نام و ورود کاربران
- لیست محصولات به همراه جزئیات
- جستجو و فیلتر محصولات
- افزودن محصولات به سبد خرید
- ثبت سفارش و پیگیری وضعیت سفارش
- پنل مدیریت برای افزودن/ویرایش محصولات
- طراحی شده با استفاده از Django Template و Bootstrap

## 🛠 تکنولوژی‌ها

- **Backend:** Django 4.x
- **Database:** SQLite (قابل تغییر به PostgreSQL)
- **Frontend:** HTML5, CSS3, Bootstrap
- **Auth:** Django built-in authentication

## 🚀 شروع سریع (لوکال)

### پیش‌نیازها

- Python 3.10 یا بالاتر
- pip
- virtualenv (اختیاری ولی توصیه‌شده)

### مراحل اجرا

```bash
# کلون کردن ریپو
git clone https://github.com/Erfan-aminian/E-Commerce.git
cd E-Commerce

# ساخت و فعال‌سازی محیط مجازی
python -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate

# نصب وابستگی‌ها
pip install -r requirements.txt

# مهاجرت دیتابیس
python manage.py migrate

# ساخت سوپر یوزر برای پنل ادمین
python manage.py createsuperuser

# اجرای سرور
python manage.py runserver
