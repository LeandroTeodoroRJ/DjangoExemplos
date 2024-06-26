from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"] #Field will be exclude
        labels = {
            "user_name": "Your Name",
            "user_name": "Your Email",
            "text": "Your Comment"

        }
