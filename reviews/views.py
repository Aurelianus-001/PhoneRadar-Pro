from django.shortcuts import render, get_object_or_404
from .models import Review

# 首页视图：展示所有测评文章
def review_list(request):
    # 从数据库拿走所有的测评文章，按时间倒序排（最新的在前面）
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

# 详情页视图：点开某一篇测评看全文
def review_detail(request, slug):
    # 根据那个唯一的 slug 找到那篇文章，找不到就报 404 错误
    review = get_object_or_404(Review, slug=slug)
    return render(request, 'reviews/review_detail.html', {'review': review})