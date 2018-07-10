# --coding:UTF-8
from django.db import models

# Create your models here.
class User(models.Model):
    SEX = (
        ('M','男'),
        ('F','女'),
        ('U','保密'),
    )
    nickname = models.CharField(max_length=64,unique=True)
    password = models.CharField(max_length=128)
    icon = models.ImageField()
    age = models.IntegerField()
    sex = models.CharField(max_length=8,choices=SEX)

<<<<<<< HEAD
    # 第三方平台上的用户信息
    platform_id = models.CharField(max_length=64)
    platform_icon = models.CharField(max_length=256)

    @property
    def avatar_url(self):
        return self.platform_icon or self.icon.url
=======
>>>>>>> 343f19cae863de0f7944cd5a59d1de5cc60fa153
