from django.db import models
from AppJob import models as modelJob
from AppUsers import models as modelUser
# Create your models here.
class Blog(models.Model):
    userID=models.ForeignKey(modelUser.users,on_delete=models.CASCADE)
    title=models.CharField(max_length=50 )
    location=models.CharField(max_length=50 )
    description=models.TextField(max_length=100 )
    

class blogImg(models.Model):
    blogID =  models.ForeignKey( Blog , on_delete=models.CASCADE )
    blogimg = models.ImageField(upload_to = "images/blog/")



class comments(models.Model):
    blogID=models.ForeignKey('Blog',on_delete=models.CASCADE) 
    commentStr=models.TextField()
    userID=models.ForeignKey(modelUser.users,on_delete=models.CASCADE)
    startTime=models.DateTimeField()


class tagsBlog(models.Model):
    tagID = models.ForeignKey(modelJob.tags , on_delete=models.CASCADE)
    blogID = models.ForeignKey(Blog , on_delete=models.CASCADE)

    class Meta:
        unique_together = (('tagID', 'blogID'))    
