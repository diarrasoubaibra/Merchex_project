from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    def __str__(self):
        return f'{self.name}'

    class Genre(models.TextChoices):
        ACTION = 'AC'
        COMEDIE = 'COM'
        DRAME = 'DRA'
        SCIENCEFICTION = 'SF'
        HORREUR = 'HOR'
        ROMANCE = 'ROM'
        THRILLER = 'THRI'
        ANIMATION = 'ANIM'

    class Type(models.TextChoices):
        Records = 'RCRD'
        Clothing = 'CLOTH'
        Posters = 'POST'
        Miscellaneous = 'MIS'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1990), MaxValueValidator(2023)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=True)
    year = models.fields.IntegerField()
    type = models.fields.CharField(choices=Type.choices, max_length=10)
