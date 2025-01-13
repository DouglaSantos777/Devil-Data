from django.db import models

class Char(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    age = models.PositiveIntegerField(blank=True, null=True)
    genre = models.CharField(max_length=20, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True, null=True)
    affiliation = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('Alive', 'Alive'), ('Dead', 'Dead'), ('Unknown', 'Unknown')], blank=True, null=True)

def __str__(self):
        return self.name

