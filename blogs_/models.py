from django.db import models

# Create your models here.
class BlogPost(models.Model):
    '''blog的组成字段'''
    title=models.CharField(max_length=200)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.title)>30:
            return self.title[:30]+'...'
        else:
            return self.title
