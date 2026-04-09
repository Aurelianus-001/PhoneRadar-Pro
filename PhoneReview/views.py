from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .models import Review, Comment

# 1. 首页视图
class ReviewListView(generic.ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    # 修正：建议保持为 'reviews'，确保和 HTML 里的 {% for review in reviews %} 对应
    context_object_name = 'reviews'
    queryset = Review.objects.all().order_by('-date_published')


# 2. 详情页视图
class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'

    # [进阶逻辑] 处理评论提交
    def post(self, request, *args, **kwargs):
        review = self.get_object()
        user_name = request.POST.get('user_name', '匿名网友')
        text = request.POST.get('text')

        if text:
            Comment.objects.create(review=review, user_name=user_name, text=text)

        return redirect('review_detail', slug=review.slug)


# 3. 处理点赞和踩
def review_vote(request, slug, vote_type):
    review = get_object_or_404(Review, slug=slug)
    if vote_type == 'like':
        review.likes += 1
    elif vote_type == 'dislike':
        review.dislikes += 1
    review.save()
    return redirect('review_detail', slug=slug)