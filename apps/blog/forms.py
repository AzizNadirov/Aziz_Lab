from django import forms
from .models import Comment, Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]
        widgets = {'content': CKEditorUploadingWidget}


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'drafted']
        widgets = {
            'content': CKEditorUploadingWidget()
        }
