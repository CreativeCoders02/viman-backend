from django.db import models
from django.contrib.auth.models import User


class TestModel(models.Model):
    name = models.CharField(max_length=100)
    emailId = models.EmailField(
        max_length=100, default="creativecoders.vitb@gmail.com")

    created_at = models.DateTimeField(auto_now_add=True)




class Room(models.Model):
    room_number = models.CharField(max_length=100)
    block_number = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.room_number


class Student(User):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=100)



class Slot(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Request(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    items = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class Proof(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='proofs/')



