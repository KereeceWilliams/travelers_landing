from django.db import models

# Create your models here.
class Question(models.Model):
  name = models.CharField(max_length=70)
  email = models.EmailField(max_length=70)
  title = models.CharField(max_length=300)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.title

class Video(models.Model):
  title = models.CharField(max_length=300)

class Survey(models.Model):
  title = models.CharField(max_length=300)