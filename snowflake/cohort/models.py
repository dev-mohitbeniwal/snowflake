from mongoengine import Document, fields
from bson.objectid import ObjectId
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
import os
from liaise.models import Tag, Vote


# To be used in uploading the image for model.ImageField
def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Badge(Document):
    # using Django enumeration types that can be subclassed to define choices in a concise way
    class CATEGORY(models.TextChoices):
        QUESTION_BADGE = 'QB', _('Question Badge')
        ANSWER_BADGE = 'AB', _('Answer Badge')
        PARTICIPATION_BADGE = 'PB', _('Participation Badge')
        TAG_BADGE = 'TB', _('Tag Badge')
        MODERATION_BADGE = 'MB', _('Moderation Badge')

    name = fields.StringField(required=True, max_length=30)
    badge_detail = fields.StringField()
    badge_category = fields.StringField(max_length=2, choices=CATEGORY.choices)


class Post(Document):
    by = fields.StringField()
    heading = fields.StringField()
    complete_post = fields.StringField()
    votes = fields.ListField(fields.ReferenceField(Vote))
    tags = fields.ListField(fields.ReferenceField(Tag))


class Developer(Document):
    first_name = fields.StringField(max_length=30)
    last_name = fields.StringField(max_length=30)
    email_id = fields.EmailField()
    profile_pic = fields.ImageField()    # models.ImageField(upload_to=get_image_path, blank=True, null=True)
    department = fields.StringField(max_length=50)
    designation = fields.StringField(max_length=50)
    developer_story = fields.StringField()
    registered_date = fields.DateTimeField(default=timezone.now)
    last_seen = fields.DateTimeField()
    bookmarks = fields.ListField(fields.ReferenceField(Post))
    tags = fields.ListField(fields.ReferenceField(Tag))
    reputation = fields.IntField()
    badges = fields.ListField(fields.ReferenceField(Badge))