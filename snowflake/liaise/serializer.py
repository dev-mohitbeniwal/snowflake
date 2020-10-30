from rest_framework_mongoengine import serializers, fields as field
from rest_framework import fields
from .models import Tag, Vote, Comment, Answer, Question


class TagSerializer(serializers.DocumentSerializer):
    tag_name = fields.CharField(required=True)
    info = fields.CharField()
    synonyms = fields.ListField()

    class Meta:
        model = Tag
        fields = '__all__'


class VoteSerializer(serializers.DocumentSerializer):
    direction = fields.BooleanField(required=True)
    by = fields.IntegerField()
    created_time = fields.DateTimeField()

    class Meta:
        model = Vote
        fields = '__all__'


class CommentSerializer(serializers.DocumentSerializer):
    by = fields.IntegerField(required=True)
    comment_text = fields.CharField()
    created_time = fields.DateTimeField()
    modified_time = fields.DateTimeField()
    votes = fields.ListField()
    comments = fields.ListField()

    class Meta:
        model = Comment
        fields = '__all__'


class AnswerSerializer(serializers.DocumentSerializer):
    answer_text = fields.CharField(required=True)
    author = fields.IntegerField()
    created_time = fields.DateTimeField()
    modified_time = fields.DateTimeField()
    tags = fields.ListField()
    comments = fields.ListField()
    votes = fields.ListField()

    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.DocumentSerializer):
    question_hdr = fields.CharField(required=True)
    question_detail = fields.CharField(required=True)
    created_time = fields.DateTimeField()
    modified_time = fields.DateTimeField()
    developer_id = fields.IntegerField()
    status = fields.IntegerField()
    tags = fields.ListField()
    votes = fields.ListField()
    views = fields.IntegerField()
    answers = fields.ListField()
    comments = fields.ListField()

    class Meta:
        model = Question
        fields = '__all__'
