from django import forms
from blog.models import blogs
from django.core.exceptions import ValidationError

class Article_name(forms.Form):
    article_name = forms.ModelChoiceField(queryset=blogs.objects.all(),empty_label="Please choose one",widget=forms.Select(
                                             attrs={'class': 'selectpicker bla bla bli',"data-live-search":"true"}))

class Post_new(forms.Form):
    title = forms.CharField(max_length=100) #New article title
    plain = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'})) #new article content
    #form validation for unique title name
    def clean_title(self):
        title = self.cleaned_data['title']
        if blogs.objects.filter(article_name=title).exists():
            raise forms.ValidationError('The article has been posted, please change another name')
        return title
