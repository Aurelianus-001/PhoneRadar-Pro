"""
Django settings for phoneradar_pro project.
"""

import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# --- 核心安全配置 ---
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-7%v9px$buqj4@7!bdq5pz!o%e7!2r3y^3y!h_)93o4%f$)^c-3')

# 在生产环境中建议改为 False
DEBUG = True

ALLOWED_HOSTS = [
    'phone-radar-pro.aurelianus.online',
    'phone-radar-pro.vercel.app',
    '.vercel.app',
    '127.0.0.1',
    'localhost',
]


# --- 应用定义 ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reviews', # 你的应用
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # 必须放在这里，负责静态文件加速
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'phoneradar_pro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], # 保持为空，Django会自动在app下的templates目录找
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'phoneradar_pro.wsgi.application'


# --- 数据库配置 (自动适配本地和 Vercel) ---
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')),
        conn_max_age=600,
        ssl_require=True if os.getenv('DATABASE_URL') else False
    )
}


# --- 密码验证与国际化 ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- 静态文件配置 (关键部分) ---
STATIC_URL = 'static/'

# 告诉 Django 除了 App 目录，还要去哪里找静态文件
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 部署时收集所有静态文件的目录 (给 Whitenoise 使用)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 启用 Whitenoise 压缩功能，提升加载速度
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'