from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Comment  # 记得导入 Comment


# 1. 首页视图
def review_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews/review_list.html', {'reviews': reviews})


# 2. 详情页视图 (增加处理评论逻辑)
def review_detail(request, slug):
    review = get_object_or_404(Review, slug=slug)

    # 如果用户提交了评论表单 (POST请求)
    if request.method == "POST":
        user_name = request.POST.get('user_name', '匿名网友')
        text = request.POST.get('text')
        if text:
            Comment.objects.create(review=review, user_name=user_name, text=text)
            return redirect('review_detail', slug=slug)  # 提交后刷新本页

    return render(request, 'reviews/review_detail.html', {'review': review})


# 3. [新增] 处理点赞和踩的视图
def review_vote(request, slug, vote_type):
    review = get_object_or_404(Review, slug=slug)
    if vote_type == 'like':
        review.likes += 1
    elif vote_type == 'dislike':
        review.dislikes += 1
    review.save()
    # 投票后跳回原来的详情页
    return redirect('review_detail', slug=slug)