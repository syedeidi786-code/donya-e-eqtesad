from django import forms
from .models import Article
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class CommentForm(forms.ModelForm):

     class Meta:

        model = Comment

        fields = ["body"]

        widgets = {
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Write your comment..."
                }
            )
        }

    class Meta:
        model = Article

        fields = [
            "title",
            "category",
            "image",
            "body",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Article title",
                }
            ),

            "category": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 12,
                    "placeholder": "Write your article here...",
                }
            ),
        }