from django import forms
from .models import NeighbourHood, Business, Post


class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')