from django.contrib import admin
from .models import Brand, PhoneModel, Review

# 1. 品牌管理界面
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    # 列表页显示哪些字段
    list_display = ('name', 'origin', 'logo_url')
    # 增加搜索功能（按名称搜）
    search_fields = ('name',)

# 2. 手机型号管理界面
@admin.register(PhoneModel)
class PhoneModelAdmin(admin.ModelAdmin):
    # 列表页显示品牌、型号和发布日期
    list_display = ('name', 'brand', 'launch_date', 'os_type')
    # 右侧增加快捷过滤器（按品牌和系统过滤）
    list_filter = ('brand', 'os_type')
    # 增加搜索功能（按型号名搜）
    search_fields = ('name',)

# 3. 测评文章管理界面
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # 列表页显示标题、作者、评分和时间
    list_display = ('title', 'author', 'rating', 'created_at')
    # 右侧增加过滤器（按评分和时间过滤）
    list_filter = ('rating', 'created_at')
    # 增加搜索功能（搜标题和内容）
    search_fields = ('title', 'content')
    # 核心高级功能：当你输入标题时，URL别名(Slug)会自动跟着生成
    prepopulated_fields = {'slug': ('title',)}
    # 横向筛选器：在多对多选择手机时，体验更好
    filter_horizontal = ('phones',)