# 📱 PhoneRadar Pro (手机雷达专业版)

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-5.0%2B-green)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

**PhoneRadar Pro** 是一个基于 Django 开发的专业手机评测内容管理系统。它旨在为数码爱好者提供一个结构化、易扩展的硬件评价平台。

---

## 🚀 核心功能

* **多维度建模**：采用 Django ORM 实现品牌 (Brand)、型号 (PhoneModel) 与测评 (Review) 的深层关联。
* **工业级后台**：深度定制的 Admin 管理界面，支持搜索、多重过滤及图片/链接管理。
* **动态渲染**：通过 MVT 架构实现测评内容的自动化实时展示。
* **SEO 友好**：内置自动生成 Slug 功能，确保每一篇测评都有美观且利于搜索的 URL。
* **对比评测**：支持一篇文章关联多个机型，满足对比横评场景。

---

## 🛠️ 技术栈

* **后端**: Python 3.10+ / Django 5.0+
* **数据库**: SQLite 3 (开发环境)
* **版本控制**: Git / GitHub
* **前端**: 原生 HTML5 / CSS3 (支持响应式布局)

---

## 📦 快速开始

如果你想在本地运行这个项目，请按照以下步骤操作：

### 1. 克隆项目

git clone [https://github.com/Aurelianus-001/PhoneRadar-Pro.git](https://github.com/Aurelianus-001/PhoneRadar-Pro.git)

cd PhoneRadar-Pro
### 2. 创建虚拟环境并安装依赖
Bash
python -m venv .venv
source .venv/bin/activate  # Windows 使用 .venv\Scripts\activate
pip install django
### 3. 初始化数据库
Bash
python manage.py makemigrations
python manage.py migrate
### 4. 创建管理员并启动
Bash
python manage.py createsuperuser
python manage.py runserver
访问 http://127.0.0.1:8000/admin 录入数据，随后在 http://127.0.0.1:8000/ 查看效果。

### 📂 项目结构预览
Plaintext
phoneradar_pro/
├── phoneradar_pro/      # 项目配置
├── reviews/             # 测评核心模块
│   ├── models.py       # 数据库模型 (核心地基)
│   ├── views.py        # 业务逻辑 (大脑)
│   ├── urls.py         # 路由配置 (门牌号)
│   └── templates/      # 网页模板 (脸面)
└── manage.py           # 项目管理入口
### 🤝 贡献与反馈
欢迎提交 Issue 或 Pull Request 来完善这个项目。如果你觉得这个项目对你有帮助，请点一个 Star ⭐！

Author: Aurelianus-001