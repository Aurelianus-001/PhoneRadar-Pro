from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from .models import Review, Comment, PhoneModel
from .forms import PhoneModelForm, ReviewForm

# 1. 首页视图
class ReviewListView(generic.ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'
    queryset = Review.objects.all().order_by('-date_published')

# 2. 详情页视图
class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'

    def post(self, request, *args, **kwargs):
        review = self.get_object()
        user_name = request.POST.get('user_name', '匿名网友')
        text = request.POST.get('text')
        if text:
            Comment.objects.create(review=review, user_name=user_name, text=text)
        return redirect('review_detail', slug=review.slug)

# 3. 点赞/踩
def review_vote(request, slug, vote_type):
    review = get_object_or_404(Review, slug=slug)
    if vote_type == 'like':
        review.likes += 1
    elif vote_type == 'dislike':
        review.dislikes += 1
    review.save()
    return redirect('review_detail', slug=slug)

# 4. 注册视图
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

# 5. 添加手机型号（仅登录用户）
class AddPhoneView(LoginRequiredMixin, CreateView):
    model = PhoneModel
    form_class = PhoneModelForm
    template_name = 'reviews/add_phone.html'
    success_url = reverse_lazy('review_list')

# 6. 添加测评（仅登录用户）
class AddReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/add_review.html'
    success_url = reverse_lazy('review_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)