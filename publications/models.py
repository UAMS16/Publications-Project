from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.


class Publication(models.Model):
    title = models.CharField(max_length=115)
    first_author_first_name = models.CharField(max_length=20)
    first_author_last_name = models.CharField(max_length=20)
    author_list = models.TextField()
    abstract = models.TextField()
    references = models.CharField(max_length=50)
    laboratory = models.CharField(max_length=50)
    journal_name = models.CharField(max_length=50)
    journal_volume = models.CharField(max_length=10)
    published_date = models.DateField("Published Date(mm/dd/yyyy)",
        auto_now_add=False, auto_now=False, blank=True, null=True
    )
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("publication-detail", kwargs={"pk": self.pk})
