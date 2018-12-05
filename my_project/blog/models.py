from django.db import models
import datetime

class blogs(models.Model):
    article_name = models.CharField('artice_name', max_length=200, primary_key=True) #this is article name, let's set it for primary_key
    plain_text = models.TextField('plain_text', null=False) #this is article, we use TextField cause it can cantain a lot.
    post_time = models.DateTimeField('post_time', default=datetime.datetime.now()) #artice post time
    #this part is set up for the forms. Talk about it later.....
    def __str__(self):
        return self.article_name