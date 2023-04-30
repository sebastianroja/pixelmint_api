from django.db import models

# Create your models here.

class test  (models.Model):
    idtest=models.IntegerField(primary_key=True, verbose_name='id de test')


    def str(self):
        return self.idtest
