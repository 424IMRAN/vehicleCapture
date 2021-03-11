from django.db import models

class Video(models.Model):
    inputName = models.CharField(max_length=200)
    initialTime = models.CharField(max_length = 200)
    file = models.FileField()



# Create your models here.

class camera(models.Model):
    
    id = models.AutoField(primary_key=True)
    camera_name = models.CharField(max_length=30)
    camera_id=models.PositiveIntegerField()
    direction_id1=models.PositiveIntegerField()
    direction_name1 = models.CharField(max_length=30)
    direction_coordinates1 = models.FloatField(max_length=30)
    direction_id2=models.PositiveIntegerField()
    direction_name2 = models.CharField(max_length=30)
    direction_coordinates2 = models.FloatField(max_length=30)
    direction_id2=models.PositiveIntegerField()
    direction_name2 = models.CharField(max_length=30)
    direction_coordinates2 = models.FloatField(max_length=30)
    direction_id3=models.PositiveIntegerField()
    direction_name3 = models.CharField(max_length=30)
    direction_coordinates3 = models.FloatField(max_length=30)
    direction_id4=models.PositiveIntegerField()
    direction_name4 = models.CharField(max_length=30)
    direction_coordinates4 = models.FloatField(max_length=30)

   