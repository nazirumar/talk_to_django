from django.db import models
from pgvector.django import VectorField
from blog import services

# Create your models here.
EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_LENGHT = 768

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    _content = models.TextField(blank=True, null=True)
    timestamp =models.DateTimeField(auto_now_add=True)
    embedding = VectorField(dimensions=EMBEDDING_LENGHT, blank=True, null=True)
    can_delete = models.BooleanField(default=False, help_text='Use in jupyter notebook')

    def save(self, *args, **kwargs):
       has_changed = False
       if self._content != self.content:
           has_changed = True
           self._content = self.content
       if (self.embedding is None) or has_changed == True:
           row_embedding_text = self.get_embedding_text_row()
           if row_embedding_text is not None:
               self.embedding = services.get_embedding(row_embedding_text)
       super().save(*args, **kwargs) # Call the real save() method
    def get_embedding_text_row(self):
        return self.content