from django.db import models
from django.utils import timezone

#class defines an object
#models.Model means Post is a Django model so Django knows to save it in the database
class Post(models.Model):
    #ForeignKey is a link to another model
    author = models.ForeignKey('auth.User')
    #text with limited number of characters
    title = models.CharField(max_length=200)
    #long text without limit
    text = models.TextField()
    #date and time
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    #def = function/method
    #publish = name of method
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
