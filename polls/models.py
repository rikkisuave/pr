from django.db import models

# Create your models here.
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
class Pagedata(models.Model):
    title=models.CharField(max_length=50)
    info=models.TextField()
    def get_title(self):
        return self.title
    def get_info(self):
        return self.info
