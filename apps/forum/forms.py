from django import forms
from .models import Question, Answer, Comment


class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']


class AnswerCreateForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']