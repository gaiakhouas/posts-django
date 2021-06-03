from django.db import models

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:20] #retourner les 20 premiers char du text

# Create your models here.
