from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
# Create your models here.
from django.db import models
from pgvector.django import VectorField


# Create your models here.
EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_LENGHT = 768


class Embedding(models.Model):
    embedding = VectorField(dimensions=EMBEDDING_LENGHT, blank=True, null=True)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp =models.DateTimeField(auto_now_add=True)
    embedding_obj = GenericRelation(Embedding)
    can_delete = models.BooleanField(default=False, help_text='Use in jupyter notebook')


    def get_embedding_text_raw(self):
        return self.content