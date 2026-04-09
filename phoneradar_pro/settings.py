"""
Django settings for phoneradar_pro project.
"""

import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# 加载环境变量 (用于本地读取 .env 文件中的 DATABASE_URL)
load_dotenv()

# 项目根目录路径
BASE_DIR = Path(__file__).resolve().parent.parent


# --- 核心安全配置 ---
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-7%v9px$buqj4@7!bdq5pz!o%e7!2r3y^3y!h_)93o4%f$)^c-3')

# 调试模式：开发时设为 True，上线前记得在 Vercel 环境变量中设为 False
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
    'reviews', # 你的业务 App
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # 静态文件中间件：必须放在 SecurityMiddleware 之后
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
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # 允许在根目录下创建通用的 templates 文件夹
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'phoneradar_pro.wsgi.application'


# --- 数据库配置 (自动适配本地 SQLite 和 线上 Postgres) ---
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

# 设置为中文（如果你喜欢中文后台）或保持 en-us
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai' # 设置为中国标准时间
USE_I18N = True
USE_TZ = True


# --- 静态文件配置 (Step 3 的核心) ---
STATIC_URL = 'static/'

# 告诉 Django 除了 App 下的 static 目录，还要去哪里找静态资源
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 部署时执行 collectstatic 命令后，所有文件汇聚的目录
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 启用 WhiteNoise 的存储后端，用于在线上高效处理静态文件（含压缩和版本化）
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'