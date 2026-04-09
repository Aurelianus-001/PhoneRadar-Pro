from django.contrib import admin
from .models import Brand, PhoneModel, Review, Comment


# 1. 品牌管理界面
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    # 对齐新字段：name, origin, manufacturing_since (老师要求)
    list_display = ('name', 'origin', 'manufacturing_since')
    search_fields = ('name',)


# 2. 手机型号管理界面
@admin.register(PhoneModel)
class PhoneModelAdmin(admin.ModelAdmin):
    # 修复报错：name -> model_name, os_type -> platform
    list_display = ('model_name', 'brand', 'launch_date', 'platform')
    list_filter = ('brand', 'platform')  # 修复报错：os_type -> platform
    search_fields = ('model_name',)


# 3. 测评文章管理界面
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # 修复报错：created_at -> date_published
    list_display = ('title', 'author', 'rating', 'likes', 'dislikes', 'date_published')
    list_filter = ('rating', 'date_published')  # 修复报错：created_at -> date_published
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

    # 修复核心报错：phones -> phone_models (多对多字段)
    filter_horizontal = ('phone_models',)

    # 保留你的高级功能：评论内联
    class CommentInline(admin.TabularInline):
        model = Comment
        extra = 0

    inlines = [CommentInline]


# 4. 评论管理界面
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'review', 'created_at', 'text_summary')
    list_filter = ('created_at',)
    search_fields = ('user_name', 'text', 'review__title')

    def text_summary(self, obj):
        return obj.text[:30] + '...' if len(obj.text) > 30 else obj.text

    text_summary.short_description = "Content Summary"