from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    titles = models.IntegerField(default=0, blank=True, null=True)
    top_scorer = models.CharField(max_length=50, blank=False, null=False)
    fifa_code = models.CharField(max_length=3, unique=True, blank=False, null=False)
    first_cup = models.DateField(blank=True, null=True)

    def __repr__(self):
        return f'<[{self.id}] {self.name} - {self.fifa_code}>'
