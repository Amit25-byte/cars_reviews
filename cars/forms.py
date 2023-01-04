from django import forms
from .models import Review
from django.forms import ModelForm
# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name',max_length=100)
#     last_name = forms.CharField(label='Last Name',max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write  review here',widget=forms.Textarea(attrs={'class':'myform'
#                                                                                      ,'rows':'5','cols':'30'}))
    
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        # fields = ['first_name','last_name','stars']
        # if you want all fields then
        fields = "__all__"

        #overwrite the Fields
        labels = {
            'first_name':'Enter your first name',
            'last_name':'Enter your last name',
            'stars':'Rate this webpage'
        }
        error_messages = {
            'stars':{
            'min_value':'OPPS! min rating must be 1',
            'max_value':'OPPS! max rating must be equal or less than 5',

            }

        }