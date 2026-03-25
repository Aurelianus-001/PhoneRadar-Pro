from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# 1. 手机品牌表
class Brand(models.Model):
    name = models.CharField("品牌名称", max_length=50, unique=True)
    origin = models.CharField("所属国家", max_length=50)
    logo_url = models.URLField("Logo链接", blank=True, help_text="可以填一个网上的图片地址")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = "品牌管理"

    def __str__(self):
        return self.name


# 2. 手机型号表
class PhoneModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models', verbose_name="所属品牌")
    name = models.CharField("型号名称", max_length=100)
    launch_date = models.DateField("发布日期")
    os_type = models.CharField("操作系统", max_length=50,
                               choices=[('iOS', 'iOS'), ('Android', 'Android'), ('Others', '其他')])

    class Meta:
        verbose_name = "手机型号"
        verbose_name_plural = "手机型号管理"

    def __str__(self):
        return f"{self.brand.name} {self.name}"


# 3. 核心：测评文章表
class Review(models.Model):
    title = models.CharField("测评标题", max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    # 多对多：一篇文章可以评测多个手机（比如对比评测）
    phones = models.ManyToManyField(PhoneModel, related_name='reviews', verbose_name="关联手机")
    content = models.TextField("正文内容")
    rating = models.PositiveIntegerField("评分(1-5)", default=5)
    created_at = models.DateTimeField("发布时间", auto_now_add=True)

    # 开源级功能：Slug 用于生成漂亮的 URL，如 /review/iphone-15-pro-vs-s24
    slug = models.SlugField("URL别名", unique=True, blank=True, max_length=250)

    class Meta:
        verbose_name = "手机测评"
        verbose_name_plural = "测评文章管理"

    # 自动生成 Slug 的逻辑
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title