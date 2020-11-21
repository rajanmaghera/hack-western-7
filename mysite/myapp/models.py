from django.db import models
from django.utils import timezone
from PIL import Image

# Create your models here.
# find person first, then get posts though ID
# from myapp.models import Person, Comment, Post
# To make a object object_name(var_name="info" ... )
# e.g Person(person_name="bob",person_text="the builder")
# To add a item, Person_object.Post_set.create()
# Works the same with the comment and post

class Person(models.Model):
    person_name = models.CharField(max_length=20,default="")
    person_text = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.person_name


class Comment(models.Model):


    comment_text = models.CharField(max_length=200,default="")

    def return_info(self):
        return self.comment_text


class Post(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, default="Nobody")
    post_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default="No picture")
    post_text = models.CharField(max_length=200, default="no text")
    # when you are getting this date, remeber to subtract to get time since last
    posted_time = models.DateTimeField("previous time")


    def __str__(self):
        return self.post_text
