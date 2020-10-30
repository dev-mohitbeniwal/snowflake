from rest_framework_mongoengine import serializers, fields as field
from rest_framework import fields
from .models import Badge, Post, Developer


class BadgeSerializer(serializers.DocumentSerializer):
    name = fields.CharField(required=True)
    badge_detail = fields.CharField()
    badge_category = fields.CharField()

    class Meta:
        model = Badge
        fields = '__all__'


class PostSerializer(serializers.DocumentSerializer):
    by = fields.CharField()
    heading = fields.CharField()
    complete_post = fields.CharField()
    votes = fields.ListField()
    tags = fields.ListField()

    class Meta:
        model = Post
        fields = '__all__'


class DeveloperSerializer(serializers.DocumentSerializer):
    first_name = fields.CharField()
    last_name = fields.CharField()
    email_id = fields.EmailField()
    profile_pic = fields.ImageField()
    department = fields.CharField()
    designation = fields.CharField()
    developer_story = fields.CharField()
    registered_date = fields.DateTimeField()
    last_seen = fields.DateTimeField()
    bookmarks = fields.ListField()
    tags = fields.ListField()
    reputation = fields.IntegerField()
    badges = fields.ListField()

    class Meta:
        model = Developer
        fields = '__all__'
