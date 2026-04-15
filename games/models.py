from django.db import models
from django.template.defaultfilters import slugify


class Platform(models.Model):
    """游戏平台，如 Nintendo Switch, PlayStation, PC 等"""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """游戏标签，如 动作、冒险、角色扮演等"""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, help_text="评分 0.0-10.0")
    image_url = models.URLField(blank=True, help_text="游戏图片URL")
    platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, null=True, blank=True, related_name='games')
    tags = models.ManyToManyField(Tag, blank=True, related_name='games')
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Review(models.Model):
    """游戏评测文章"""
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    author = models.CharField(max_length=100, default="Anonymous")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title