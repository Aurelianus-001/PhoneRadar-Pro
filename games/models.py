from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, help_text="评分 0.0-10.0")
    image_url = models.URLField(blank=True, help_text="游戏图片URL")

    def __str__(self):
        return self.name