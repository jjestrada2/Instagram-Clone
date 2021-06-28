""" Posts Models """
#Django
from users.models import Profile
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ForeignKey('users.Profile',on_delete=models.CASCADE)
    title= models.CharField(max_length=255)
    photo=models.ImageField(upload_to='post/photos')
    created=models.DateField(auto_now_add=True)
    modified=models.DateField(auto_now=True)

    def __str__(self):
        return '{} by @{}'.format(self.title,self.user.username)
    