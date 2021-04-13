from django.db import models
from uuid import uuid4

# Create your models here.


class Books(model.Models):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titile = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
