from datetime import datetime
from django.db import models

from member.models import Member

# Create your models here.
class Fboard(models.Model):    
    b_no = models.IntegerField(default=0, primary_key=True)
    member = models.ForeignKey(Member,on_delete = models.DO_NOTHING, null = True)
    # on_delete = primary key을 제거 했을 때 foreign key는 어떻게 할 것인가? 
    # b_id = models.CharField(max_length=100)
    b_title = models.CharField(max_length=1000)
    b_content = models.TextField()
    b_date = models.DateTimeField(default = datetime.now(), blank= True)
    
    b_group = models.IntegerField(default=0)
    b_step = models.IntegerField(default=0)
    b_indent = models.IntegerField(default=0)
    
    b_hit = models.IntegerField(default=1)
    b_img = models.ImageField(blank = True)
    
    def __str__(self):
        return self.b_title