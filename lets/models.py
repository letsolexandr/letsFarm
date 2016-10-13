from django.db import models

class Balans(models.Model):
    name=models.CharField(max_length=200,verbose_name='Адреса')
    def __str__(self):
        return self.name
