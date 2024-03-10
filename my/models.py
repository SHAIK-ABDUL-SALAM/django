from django.db import models

# Create your models here.
class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    comment=models.TextField(max_length=216)
    class Meta:
        db_table="Feedback"

