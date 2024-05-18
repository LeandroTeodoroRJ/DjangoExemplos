from django import forms
from .models import ReviewModel

#Create a simple Form
#class ReviewForm(forms.Form):
#    user_name = forms.CharField(
#        label="Your Name",
#        max_length=100
#        )
#    review_text = forms.CharField(
#        label="Your Feedback",
#        widget=forms.Textarea,
#        max_length=200
#        )
#    rating = forms.IntegerField(
#        label="Your Rating",
#        min_value = 1, max_value = 5
#        )

#Creating a FormModel - connect form to model
class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = "__all__"
        # exclude = ['<field_name>']  --To exclude a field to form
        # Selecting one to one fields
        # fiels = ["user_name", "review_text", "rating"]

        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }


#The fields by default is required=True
#Form CharField official Doc: https://docs.djangoproject.com/en/5.0/ref/forms/fields/
