from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class  Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    is_finished = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
class ass(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='notes/pdfs/')
    cover = models.ImageField(upload_to="notes/covers/", null=True, blank = True)
    
    def __str__(self):
        return self.title
    
    def delete(self, *args,  **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)


    
class exx(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='experi/pdfs/')
    cover = models.ImageField(upload_to="experi/covers/", null=True, blank = True)
    
    def __str__(self):
        return self.title
    
    def delete(self, *args,  **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
        

    

