from django.db import models

# Create your models here.
class Books(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100, blank=False, unique=False)
    AuthorID = models.IntegerField()
    GenreID = models.IntegerField()
    Rating = models.IntegerField()
    Details = models.CharField(max_length=500, blank=True, unique=False)
    CreateDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateTimeField(auto_now=True)


class Author(models.Model):
    AuthorID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, blank=False, unique=False)
    Surname = models.CharField(max_length=50, blank=False, unique=False)
    Country = models.CharField(max_length=50, blank=False, unique=False)
    DateOfBirth = models.DateField()
    Details = models.CharField(max_length=500, blank=True, unique=False)
    CreateDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateTimeField(auto_now=True)


class Genre(models.Model):
    GenreID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, blank=False, unique=False)
    Details = models.CharField(max_length=500, blank=True, unique=False)
    CreateDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateTimeField(auto_now=True)
