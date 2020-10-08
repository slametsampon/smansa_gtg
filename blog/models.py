from django.db import models

# Create your models here.

from datetime import date
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from accounts.models import SmansaUser

class Blog(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(SmansaUser, on_delete=models.SET_NULL, null=True)
      # Foreign Key used because Blog can only have one author/SmansaUser, but bloggsers can have multiple blog posts.
    description = models.TextField(max_length=2000, help_text="Enter you blog text here.")
    post_date = models.DateField(default=date.today)
    
    class Meta:
        ordering = ["-post_date"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular blog instance.
        """
        return reverse('blog:blog-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
        
        
class BlogComment(models.Model):
    """
    Model representing a comment against a blog post.
    """
    description = models.TextField(max_length=1000, help_text="Enter comment about blog here.")
    author = models.ForeignKey(SmansaUser, on_delete=models.SET_NULL, null=True)
      # Foreign Key used because BlogComment can only have one author/SmansaUser, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title=75
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring
