from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from .models import Review, Comment, PhoneModel, Brand
from .forms import PhoneModelForm, ReviewForm

# ---------- 首页（网站介绍）----------
class HomeView(TemplateView):
    template_name = 'home.html'

# ---------- 手机测评部分 ----------
# 品牌列表页（所有品牌）
class BrandListView(generic.ListView):
    model = Brand
    template_name = 'reviews/brand_list.html'
    context_object_name = 'brands'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_module'] = 'phone'
        context['current_subpage'] = 'brand_list'
        return context

# 品牌下的型号列表页
class BrandPhoneModelListView(generic.DetailView):
    model = Brand
    template_name = 'reviews/brand_models.html'
    context_object_name = 'brand'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['models'] = self.object.models.all()
        context['current_module'] = 'phone'
        # 此页面不属于三个主菜单之一，不设置 current_subpage
        return context

# 所有手机型号列表页
class AllPhoneModelListView(generic.ListView):
    model = PhoneModel
    template_name = 'reviews/all_models.html'
    context_object_name = 'models'
    ordering = ['brand__name', 'model_name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_module'] = 'phone'
        context['current_subpage'] = 'all_models'
        return context

# 型号详情页（显示该型号的所有测评）
class PhoneModelDetailView(generic.DetailView):
    model = PhoneModel
    template_name = 'reviews/phonemodel_detail.html'
    context_object_name = 'phonemodel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_module'] = 'phone'
        context['current_subpage'] = 'all_models'   # 高亮左侧“All Phone Models”
        return context

# 手机测评文章列表页
class ReviewListView(generic.ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'
    queryset = Review.objects.all().order_by('-date_published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_module'] = 'phone'
        context['current_subpage'] = 'review_list'
        return context

# 测评详情页
class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'

    def post(self, request, *args, **kwargs):
        review = self.get_object()
        user_name = request.POST.get('user_name', 'Anonymous')
        text = request.POST.get('text')
        if text:
            Comment.objects.create(review=review, user_name=user_name, text=text)
        return redirect('review_detail', slug=review.slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_module'] = 'phone'
        return context

# 点赞/踩
def review_vote(request, slug, vote_type):
    review = get_object_or_404(Review, slug=slug)
    if vote_type == 'like':
        review.likes += 1
    elif vote_type == 'dislike':
        review.dislikes += 1
    review.save()
    return redirect('review_detail', slug=slug)

# ---------- 用户认证 ----------
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

# ---------- 添加数据（仅登录用户）----------
class AddPhoneView(LoginRequiredMixin, CreateView):
    model = PhoneModel
    form_class = PhoneModelForm
    template_name = 'reviews/add_phone.html'
    success_url = reverse_lazy('all_models')

class AddReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/add_review.html'
    success_url = reverse_lazy('review_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)