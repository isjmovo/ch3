from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_Data = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    qustion = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str(self):
        return self.choice_text