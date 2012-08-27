from django.db import models
from django.template.defaultfilters import slugify


class Ethnicity(models.Model):
    description = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

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
    address = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:50]

        return super(Student, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=20)
    students = models.ManyToManyField(Student, related_name="courses")
    
    def __unicode__(self):
        return self.name


