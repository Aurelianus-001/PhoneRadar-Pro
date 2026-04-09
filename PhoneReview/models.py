from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Brand(models.Model):
    # 老师要求：name, origin, manufacturing since
    name = models.CharField("Brand Name", max_length=50, unique=True)
    origin = models.CharField("Country", max_length=50)
    manufacturing_since = models.IntegerField("Manufacturing Since")  # 新增：老师要求的字段
    logo_url = models.URLField("Logo URL", blank=True)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name


class PhoneModel(models.Model):
    # 老师要求：brand, model name, launch date, platform
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models', verbose_name="Brand")
    model_name = models.CharField("Model Name", max_length=100)  # 改名：对齐老师的 model_name
    launch_date = models.DateField("Launch Date")
    platform = models.CharField("Platform", max_length=50,
                                choices=[('iOS', 'iOS'), ('Android', 'Android'),
                                         ('Others', 'Others')])  # 改名：对齐老师的 platform

    class Meta:
        verbose_name = "Phone Model"
        verbose_name_plural = "Phone Models"

    def __str__(self):
        return f"{self.brand.name} {self.model_name}"


class Review(models.Model):
    # 老师要求：title, content, date published, Many-to-Many with Model
    title = models.CharField("Title", max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")

    # 核心要求：多对多关系 (Review and Model)
    phone_models = models.ManyToManyField(PhoneModel, related_name='reviews', verbose_name="Related Phone Models")

    content = models.TextField("Content")
    rating = models.PositiveIntegerField("Rating(1-5)", default=5)
    date_published = models.DateTimeField("Date Published", auto_now_add=True)  # 改名：对齐老师的 date_published

    # 你之前的功能字段
    slug = models.SlugField("URL Slug", unique=True, blank=True, max_length=250)
    likes = models.PositiveIntegerField("Likes", default=0)
    dislikes = models.PositiveIntegerField("Dislikes", default=0)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments', verbose_name="Review")
    user_name = models.CharField("Username", max_length=50, default="Anonymous")
    text = models.TextField("Comment")
    created_at = models.DateTimeField("Posted At", auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['-created_at']