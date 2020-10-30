from mongoengine import Document, fields
from django.utils import timezone


# Create your models here.
class Tag(Document):
    tag_name = fields.StringField(required=True, max_length=30)
    info = fields.StringField()
    synonyms = fields.ListField(field=fields.StringField())


class Vote(Document):
    direction = fields.BooleanField()
    by = fields.ObjectId()  # models.ForeignKey('cohort.Developer', on_delete=models.CASCADE)
    created_time = fields.DateTimeField(default=timezone.now) # models.DateTimeField(default=timezone.now)


class Comment(Document):
    by = fields.ObjectId(required=True)  # models.ForeignKey('cohort.Developer', on_delete=models.CASCADE)
    comment_text = fields.StringField(required=True)
    created_time = fields.DateTimeField(default=timezone.now)
    modified_time = fields.DateTimeField(default=timezone.now)
    votes = fields.ListField(fields.ReferenceField(Vote))
    comments = fields.ListField(fields.ObjectId())


class Answer(Document):
    answer_text = fields.StringField(required=True)
    author = fields.ObjectId()  # models.ForeignKey('cohort.Developer', on_delete=models.CASCADE)
    created_time = fields.DateTimeField(default=timezone.now)
    modified_time = fields.DateTimeField(default=timezone.now)
    tags = fields.ListField(fields.ReferenceField(Tag))
    comments = fields.ListField(fields.ReferenceField(Comment))
    votes = fields.ListField(fields.ReferenceField(Vote))


class Question(Document):
    QUESTION_STATUS = ((1, 'Active'), (0, 'Inactive'))
    question_hdr = fields.StringField(required=True)
    question_detail = fields.StringField(required=True)
    created_time = fields.DateTimeField(default=timezone.now)  # models.DateTimeField(default=timezone.now)
    modified_time = fields.DateTimeField(default=timezone.now)
    developer_id = fields.ObjectId()    # ForeignKey('cohort.Developer', on_delete=models.CASCADE)
    status = fields.IntField(choices=QUESTION_STATUS)    # models.SmallIntegerField(choices=QUESTION_STATUS)
    tags = fields.ListField(fields.ReferenceField(Tag))     # models.ManyToManyField(Tag)
    votes = fields.ListField(fields.ReferenceField(Vote))   # ArrayField(models.IntegerField())
    views = fields.IntField(min_value=0)
    answers = fields.ListField(fields.ReferenceField(Answer))
    comments = fields.ListField(fields.ReferenceField(Comment))
