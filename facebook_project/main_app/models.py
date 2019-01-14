from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length=400)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
	follows = models.ManyToManyField('UserProfileInfo', related_name='followed_by', symmetrical=False, blank=True)

	def __str__(self):
		return (self.user.username +' '+ str(self.id))