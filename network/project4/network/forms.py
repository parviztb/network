
from django import forms
from django import post, follower



class PostList(forms.ModelForm):
    class Meta:
        model = post
        fields = ['author', 'title','des_content','likes']


