from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

ROLES = {
    'PRESIDENT': 1,
    'NORMAL': 2
}


class Profile(models.Model):
    # if user is delete, also delete profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # default user role is a normal user, and can only update by super admin
    role = models.PositiveSmallIntegerField(default=ROLES['NORMAL'])

    def __str__(self):
        return f'{self.user.username} Profile'

    # overrite the save method
    def save(self, *args, **kwargs):
        # run parent save method
        super().save(*args, **kwargs)

        # resize profile image
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
