from web.models import Post
from django import forms


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'slug': forms.TextInput(attrs={'readonly': True})
        }
