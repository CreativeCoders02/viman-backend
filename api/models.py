from django.db import models

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

