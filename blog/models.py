#Where did line 2 and 4 come from? Only line 3 was defaulted 
from django.conf import settings
from django.db import models
from django.utils import timezone

#How do you know you need this? Was given by the tutorial (line 7-19)
class Post(models.Model): #Defines the model (is an object) 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title