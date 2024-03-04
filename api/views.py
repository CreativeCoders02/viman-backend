from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TestModel, Slot, Request
from .serializers import TestSerializer, SlotPostSerializer, RequestGetSerializer, SlotGetSerializer, UserSerializer
from .gpt import getUserMessage
from .mail.push_mail import push_mail

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,BasicAuthentication,BaseAuthentication,SessionAuthentication
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate

class TestView(APIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer

    def get(self, request, format=None):
        predictions = TestModel.objects.all()
        serializer = TestSerializer(predictions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            data = serializer.data
            content = getUserMessage(data['name'])
            para = content.split("\n")
            data['Response Message'] = content

            push_mail("Welcome to creative coders", data["emailId"],
                      "main.html", {"paragraphs": para})

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SlotView(APIView):
    queryset = Slot.objects.all()
    serializer_class = SlotPostSerializer

    def get(self, request, format=None):
        slot = Slot.objects.all()
        serializer = SlotGetSerializer(slot, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SlotPostSerializer(data=request.data)
        if serializer.is_valid():                                                                
            serializer.save()

            data = serializer.data

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestView(APIView):
    queryset = Request.objects.all()
    serializer_class = RequestGetSerializer
    # authentication_classes = [TokenAuthentication,BasicAuthentication,SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        requests = Request.objects.all()
        serializer = RequestGetSerializer(requests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RequestGetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            data = serializer.data
            # Perform any additional logic or operations here

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid()
        data = serializer.data
        user = None


        email = data["email"]
        username = data["username"]
        password = data["password"]
        if email:
            foundUser = User.objects.get(
                email=email)
            
            if foundUser:
                user = authenticate(username=foundUser.username,password=password)

        if username:
            user =  authenticate(username=username,password=password)

        print("USER",user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)

    def get(self, request):
        return Response([])


