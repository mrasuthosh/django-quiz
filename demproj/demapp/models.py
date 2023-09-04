from django.db import models
import uuid
import random

# Create your models here.


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable = False)
    cdate = models.DateField(auto_now=True)
    update = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Categoery(BaseModel):
    categoery_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.categoery_name

class Qusetion(BaseModel):
    ctrgy = models.ForeignKey(Categoery,related_name = 'categoery',on_delete = models.CASCADE)
    categoery_qstn = models.CharField(max_length = 100)
    makrs = models.IntegerField(default = 5)

    def __str__(self) -> str:
        return self.categoery_qstn
    
    def get_answers(self):
        ansewr_objs = list(Answer.objects.filter(question = self))
        random.shuffle(ansewr_objs)
        data = []
        for i in ansewr_objs:
            data.append(
                {
                    'answer' : i.answ,
                    'is_correct' : i.is_correct
                }
            )
        return data

class Answer(BaseModel):
    question = models.ForeignKey(Qusetion,related_name='question_answers',on_delete=models.CASCADE)
    answ = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answ
