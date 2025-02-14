from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER =(
    ('M','MALE'),
    ('F','FEMALE'),
)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=GENDER)
    image = models.ImageField(default="https://gravatar.com/avatar/d99c0abcac45067cd4aa33bbf87bb4f8?s=200&d=mp&r=x",upload_to='profile', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return self.user.username

