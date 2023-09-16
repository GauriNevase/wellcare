from django.db import models
from django.contrib.auth.models import User
class Diary_entry(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Diary_entry #{}'.format(self.id)
    
    class Meta:
        verbose_name_plural='entries'
    
class Diary(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)+'|'+str(self.date)