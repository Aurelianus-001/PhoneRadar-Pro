from django.contrib import admin
from .models import Platform, Tag, Game, Review

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'rating', 'platform')
    prepopulated_fields = {'slug': ('name',)}  # 自动填充 slug

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'game', 'rating', 'author', 'created_at')