from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class deepfake_video_detection(models.Model):

    Fid= models.CharField(max_length=300)
    video_id= models.CharField(max_length=300)
    title= models.CharField(max_length=300)
    channel_title= models.CharField(max_length=300)
    publish_time= models.CharField(max_length=300)
    tags= models.CharField(max_length=300)
    views= models.CharField(max_length=300)
    likes= models.CharField(max_length=300)
    dislikes= models.CharField(max_length=300)
    thumbnail_link= models.CharField(max_length=300)
    description= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



