from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class CustomeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('roolno')
    def get_roolno(self,param):
        return super(CustomeManager, self).get_roolno().filter(roolno__contain=param)

class ContactInfo(models.Model):
    fname = models.CharField(u'Enter First Name',max_length=60)
    lname = models.CharField(u'Enter Last Name',max_length=60)
    father_name = models.CharField(u'Enter Your Father Name',max_length=60)
    course = models.CharField(u'Enter Course Name',max_length=60)
    school_name = models.CharField(u'Enter School Name',max_length=60)
    class Meta:
        abstract = True


class StudentRegister(ContactInfo):
    roolno = models.IntegerField(u'Enter Rool Number')
    email = models.EmailField(u'Enter Email')
    objects = CustomeManager()
    def __str__(self):
        return self.fname

class ProxyStudentRegister(StudentRegister):
    class Meta:
        proxy = True

class MarksDetails(ContactInfo):
    Telugu = models.IntegerField()
    Hindi = models.IntegerField()
    English = models.IntegerField()
    Mathametics = models.IntegerField()
    Social = models.IntegerField()
    PS = models.IntegerField(u'Pysical Science')
    NS= models.IntegerField(u'Natural Science')

class Post(models.Model):
    STATUS_CHOICE = (('default','Default'),('publish','Publish'))
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=265,unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICE,default='draft')

    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title