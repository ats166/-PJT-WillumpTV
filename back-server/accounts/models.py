from django.contrib.auth.models import AbstractUser
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.validators import MinValueValidator


def genre_default():
    return {'12': 0, '14': 0, '16': 0, '18': 0, '27': 0, '28': 0, '35': 0, '36': 0, '37': 0, '53':0, '80': 0, '99':0, '878':0, '9648':0, '10402':0, '10749':0, '10751':0, '10752':0, '10770':0 }
# Create your models here.
class User(AbstractUser):
    genre_dict = models.JSONField(default=genre_default)
    # 추가한 필드 : profile_image, point
    profile_image = ProcessedImageField(
        blank=True,
        upload_to='profile_image/%Y/%m',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 70},
    )

    point = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
    )
    nickname = models.CharField(max_length=30, null=True)
    age = models.IntegerField(default=0, null=True)
    

    def __str__(self):
        return self.username
    