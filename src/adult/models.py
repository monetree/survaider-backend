from django.db import models


class Adult(models.Model):

    adult      = models.CharField(max_length=256)
    workclass =models.CharField(max_length=256)
    fnlwgt=models.CharField(max_length=256)
    education=models.CharField(max_length=256)
    Education_num=models.CharField(max_length=256)
    Marital_status=models.CharField(max_length=256)
    occupation=models.CharField(max_length=256)
    relationship=models.CharField(max_length=256)
    race=models.CharField(max_length=256)
    sex=models.CharField(max_length=256)
    Capital_gain=models.CharField(max_length=256)
    Capital_loss=models.CharField(max_length=256)
    Hours_per_week=models.CharField(max_length=256)
    Native_country=models.CharField(max_length=256)
    salary=models.CharField(max_length=256)

    class Meta:
       managed = True
       db_table = 'adult'
