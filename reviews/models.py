from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Brand(models.Model):
    name = models.CharField("Brand Name", max_length=50, unique=True)
    origin = models.CharField("Country", max_length=50)
    logo_url = models.URLField("Logo URL", blank=True)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name


class PhoneModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models', verbose_name="Brand")
    name = models.CharField("Model Name", max_length=100)
    launch_date = models.DateField("Launch Date")
    os_type = models.CharField("OS", max_length=50,
                               choices=[('iOS', 'iOS'), ('Android', 'Android'), ('Others', 'Others')])

    class Meta:
        verbose_name = "Phone Model"
        verbose_name_plural = "Phone Models"

    def __str__(self):
        return f"{self.brand.name} {self.name}"


class Review(models.Model):
    title = models.CharField("Title", max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    phones = models.ManyToManyField(PhoneModel, related_name='reviews', verbose_name="Related Phones")
    content = models.TextField("Content")
    rating = models.PositiveIntegerField("Rating(1-5)", default=5)
    created_at = models.DateTimeField("Published At", auto_now_add=True)
    slug = models.SlugField("URL Slug", unique=True, blank=True, max_length=250)

    # Voting Fields
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