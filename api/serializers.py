from rest_framework import serializers
from .models import TestModel, Slot, Request, Proof,Room,Student
from django.contrib.auth.models import User


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ["name", "emailId"]


class RoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Room
        fields = ["room_number", "block_number"]

class SlotPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Slot
        fields = ["room", "start_time", "end_time"]

class SlotGetSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    class Meta:
        model = Slot
        fields = ["room", "start_time", "end_time"]



class ProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proof
        fields = ["image"]


class StudentSerializer(serializers.ModelSerializer):
    # proof = ProofSerializer(many=True)
    class Meta:
        model = Student
        fields = ["username","first_name","last_name"]

class RequestGetSerializer(serializers.ModelSerializer):
    # proof = ProofSerializer(many=True)
    student =StudentSerializer()
    class Meta:
        model = Request
        fields = ["id", "student", "slot", "items", "status","student" ]





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
