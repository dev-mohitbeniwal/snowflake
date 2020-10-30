from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from bson import ObjectId
from django.http import Http404
from .models import *
from .serializer import *


class APIInterface(APIView):
    def __init__(self, object_model, object_serializer):
        self.ObjectModel = object_model
        self.ObjectSerializer = object_serializer

    def get_object(self, pk):
        try:
            pk = ObjectId(pk)
            return self.ObjectModel.objects.get(pk=pk)
        except self.ObjectModel.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            pk = ObjectId(pk)
            tag = self.get_object(pk)
            serializer = self.ObjectSerializer(tag)
        else:
            tag = self.ObjectModel.objects.all()
            serializer = self.ObjectSerializer(tag, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        serializer = self.ObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        pk = ObjectId(pk)
        tag = self.get_object(pk)
        serializer = self.ObjectSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pk = ObjectId(pk)
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagAPI(APIInterface):
    def __init__(self):
        super().__init__(Tag, TagSerializer)


class VoteAPI(APIInterface):
    def __init__(self):
        super().__init__(Vote, VoteSerializer)


class CommentAPI(APIInterface):
    def __init__(self):
        super().__init__(Comment, CommentSerializer)


class AnswerAPI(APIInterface):
    def __init__(self):
        super().__init__(Answer, AnswerSerializer)


class QuestionAPI(APIInterface):
    def __init__(self):
        super().__init__(Question, QuestionSerializer)

