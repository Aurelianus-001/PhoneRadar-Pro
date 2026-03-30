from django.contrib import admin
from .models import Brand, PhoneModel, Review, Comment  # 确保导入了 Comment


# 1. 品牌管理界面
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin', 'logo_url')
    search_fields = ('name',)


# 2. 手机型号管理界面
@admin.register(PhoneModel)
class PhoneModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'launch_date', 'os_type')
    list_filter = ('brand', 'os_type')
    search_fields = ('name',)


# 3. 测评文章管理界面
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # [增加] 在后台列表页直接看到点赞和踩的数量
    list_display = ('title', 'author', 'rating', 'likes', 'dislikes', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('phones',)

    # [高级功能] 在查看文章时，直接在下方列出该文章的所有评论，方便快速删除差评
    class CommentInline(admin.TabularInline):
        model = Comment
        extra = 0  # 默认不额外增加空白行

    inlines = [CommentInline]


# 4. [新增] 评论管理界面
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # 显示谁在什么时候评论了哪篇文章
    list_display = ('user_name', 'review', 'created_at', 'text_summary')
    list_filter = ('created_at',)
    search_fields = ('user_name', 'text', 'review__title')

    # 定义一个显示函数，防止评论太长撑破表格
    def text_summary(self, obj):
        return obj.text[:30] + '...' if len(obj.text) > 30 else obj.text

    text_summary.short_description = "评论内容摘要"