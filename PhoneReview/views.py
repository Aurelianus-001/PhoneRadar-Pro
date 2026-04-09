from django.shortcuts import get_object_or_404, redirect
from django.views import generic  # 导入通用视图
from .models import Review, Comment


# 1. 首页视图：使用 ListView
class ReviewListView(generic.ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'PhoneReview'
    # 这里的 queryset 替代了原来的 Review.objects.all().order_by(...)
    queryset = Review.objects.all().order_by('-created_at')


# 2. 详情页视图：使用 DetailView
class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'

    # [进阶逻辑] 在类视图中处理 POST 评论请求
    def post(self, request, *args, **kwargs):
        review = self.get_object()  # 获取当前这篇文章
        user_name = request.POST.get('user_name', '匿名网友')
        text = request.POST.get('text')

        if text:
            Comment.objects.create(review=review, user_name=user_name, text=text)

        # 提交后重定向回当前详情页
        return redirect('review_detail', slug=review.slug)


# 3. 处理点赞和踩的视图 (保持函数视图，因为它只负责逻辑重定向)
def review_vote(request, slug, vote_type):
    review = get_object_or_404(Review, slug=slug)
    if vote_type == 'like':
        review.likes += 1
    elif vote_type == 'dislike':
        review.dislikes += 1
    review.save()
    return redirect('review_detail', slug=slug)