from django import forms
from .models import PhoneModel, Review, Brand

class PhoneModelForm(forms.ModelForm):
    class Meta:
        model = PhoneModel
        fields = ['brand', 'model_name', 'launch_date', 'platform']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].queryset = Brand.objects.all()

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'phone_models', 'content', 'rating']
        widgets = {
            'phone_models': forms.CheckboxSelectMultiple,
            'content': forms.Textarea(attrs={'rows': 5}),
        }