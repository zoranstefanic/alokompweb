from django.db import models
from django.contrib.auth.models import User
from random import choice

class NewsItem(models.Model):
    """One news article on the News page"""
    title = models.CharField(max_length=300) 
    slug = models.SlugField(null=True,unique=True) 
    text = models.TextField() 
    created = models.DateField(editable=True)
    published  = models.BooleanField(default=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='NewsItems')

    class Meta:
        ordering = ["-created"]

    def __unicode__(self):
        return "%s" % self.title

    def __str__(self):
        return "%s" % self.title

    def get_photo(self):
        return choice(self.photos.all())

class Photo(models.Model):
    """Photo related to the Article"""
    caption = models.CharField(max_length=200,help_text="Photo caption",null=True) 
    image = models.FileField(upload_to="uploads/%Y")
    article = models.ForeignKey(NewsItem,on_delete=models.CASCADE,related_name="photos",null=True)
   
    def __unicode__(self):
        return "%s" %self.description

class File(models.Model):
    """File related to the Article, presentation, pdf... """
    description = models.CharField(max_length=200,help_text="Describe the file?") 
    file = models.FileField(upload_to="uploads/%Y")
    article = models.ForeignKey(NewsItem,on_delete=models.CASCADE,related_name="files",null=True)
   
    def __unicode__(self):
        return "%s" %self.description
