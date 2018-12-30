from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from django.contrib.auth.models import User

from markdownx.models import MarkdownxField

from django_countries import countries


# Create your models here.

class conference_form(models.Model):
    conference_name = models.CharField(max_length=120)
    conference_acronym = models.CharField(max_length=20)
    conference_webpage = models.URLField()
    conference_venue = models.CharField(max_length=120)
    conference_city = models.CharField(max_length=100)
    conference_country = CountryField()
    conference_start = models.DateField()
    conference_end = models.DateField()
    conference_organizer = models.CharField(max_length=120)
    conference_organizer_webpage = models.CharField(max_length=120)
    conference_organizer_contact = models.IntegerField()
    conference_research_area = models.CharField(max_length=120)
    conference_area_notes = models.TextField()
    conference_other_info = models.TextField()
    conference_author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)


    def __str__(self):
        return self.conference_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})
