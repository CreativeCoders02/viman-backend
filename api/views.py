from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TestModel
from .serializers import TestSerializer
from .gpt import getUserMessage
from .mail.push_mail import push_mail


class PredictionAPIView(APIView):
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
