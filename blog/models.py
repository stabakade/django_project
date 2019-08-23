from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #here timezone will be preferable instead of datetime
    author = models.ForeignKey(User, on_delete=models.CASCADE) #foreign key use karenge har author ko store karne ke liye, Users data will be stored in User model, on_delete will specify what happens when User gets deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return reverse('blog-home')  #gives the url of that instance as a string, this will redirect it to the home page
        return reverse('post_detail', kwargs={'pk': self.pk})
