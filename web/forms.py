from django import forms
from taggit_labels.widgets import LabelWidget

from web.models import Post, Project, ProjectImage
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
            'slug': forms.TextInput(attrs={'readonly': True}),
            'tech': LabelWidget(model=TagProject)
        }


class ProjectImageForm(forms.ModelForm):

    class Meta:
        model = ProjectImage
        fields = '__all__'
        widgets = {
            'width': forms.Select()
        }