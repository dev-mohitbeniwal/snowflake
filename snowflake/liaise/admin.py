from django_mongoengine import mongo_admin as admin
from .models import Tag, Vote, Comment, Answer, Question


# Register your models here.
admin.site.register(Tag)
admin.site.register(Vote)
admin.site.register(Comment)
admin.site.register(Answer)
admin.site.register(Question)
