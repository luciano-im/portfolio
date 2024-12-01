from django import forms
from taggit_labels.widgets import LabelWidget

from web.models import Post, Project
from web.models import TagPost, TagProject


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'slug': forms.TextInput(attrs={'readonly': True}),
            'tags': LabelWidget(model=TagPost)
        }


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'tech': LabelWidget(model=TagProject)
        }
