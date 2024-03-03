from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=100)
    emailId = models.EmailField(
        max_length=100, default="creativecoders.vitb@gmail.com")

    created_at = models.DateTimeField(auto_now_add=True)
