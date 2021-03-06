from django.db import models
from django.contrib.auth.models import Group,User
from django.template.defaultfilters import slugify
from datetime import datetime


class Ethnicity(models.Model):
    description = models.CharField(max_length=50)
    code = models.CharField(max_length=2,unique=True)

    def __unicode__(self):
        return self.description


class Student(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateTimeField('birthday')
    GENDER_CHOICES = (
        ("MA","MALE"),
        ("FE","FEMALE"),
    )
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES,
                             default="MA")
    ethnicity = models.ForeignKey(Ethnicity)
    phone = models.CharField(max_length=20)
    cell_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    comments = models.TextField(blank=True,max_length=300)
    email = models.EmailField(max_length=254,unique=True)
    slug = models.SlugField(blank=True,editable=False)
    password = models.CharField(max_length=20)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:50]
        
        new_user, created = User.objects.get_or_create(email=self.email)
        if created:
            student_group = Group.objects.get(name__startswith="students")
            new_user.set_password(self.password)
            new_user.username = self.email
            new_user.groups.add(student_group)
            new_user.save()

        return super(Student, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=20)
    students = models.ManyToManyField(Student, related_name="courses",blank=True)
    
    def __unicode__(self):
        return self.name


class Notification(models.Model):
    text = models.TextField(max_length=500)
    subject = models.CharField(max_length=40)
    date_created = models.DateTimeField('Created',default=datetime.now())
    expiration_date = models.DateTimeField('Expires')

    def __unicode__(self):
        return self.subject


class Grade(models.Model):
    grade = models.IntegerField(help_text="please select a value between 1-10")
    student = models.ForeignKey(Student,related_name="grade_student")
    course = models.ForeignKey(Course,related_name="course")
    
    class Meta:
        unique_together=(('course','student'),)

    def __unicode__(self):
        return "Student:"+self.student.name+" grade:"+str(self.grade)+" @course:"+self.course.name 


class Document(models.Model):
    code = models.CharField(max_length=2,unique=True)
    description = models.CharField(max_length=50)

    def __unicode__(self):
        return self.description


class DocumentEnquiry(models.Model):
    PROCESS_STATUS = (
        ("NE","New enquiry"),
        ("SB","Submitted for processing"),
        ("RE","Application Rejected"),
        ("CL","Closed"),
    )
    status = models.CharField(max_length=2,choices=PROCESS_STATUS ,
                             default="NE")
    document = models.ForeignKey(Document,related_name="document_type")
    student = models.ForeignKey(Student,related_name="document_student")

    def __unicode__(self):
        return self.document.description + " for " + self.student.name



