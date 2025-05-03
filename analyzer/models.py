from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    education = models.TextField()
    hobbies = models.TextField()
    lifestyle = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name