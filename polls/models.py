from django.db import models

# models represents a table in a DB
# columns are represented by a Field, class, which defines DB column data type

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # pub_date has a "human readable" note attached to it. Useful for API docs.
    pub_date = models.DateTimeField("date published")
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)     
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    