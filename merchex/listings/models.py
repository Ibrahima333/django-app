from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Band(models.Model):
    name= models.fields.CharField(max_length=100)
    title = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=50)
    biography =models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900),MaxValueValidator(2026)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True,blank=True)
     


    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        RAP = 'RP'
        
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)

# Ne serait-il pas préférable qu'au lieu d'afficher « Band object (id number) », nous puissions afficher quelque chose de plus significatif ? Pourquoi pas le nom du groupe ?
# Pour ce faire, nous pouvons éditer la représentation de la chaîne de caractères du modèle Band en modifiant sa méthode intégrée__str__.
    def __str__(self):
        return f'{self.name}'
    



class Listing(models.Model):
    class listingType(models.TextChoices) :
        RECORD = 'R'
        CLOTHINGS = 'C'
        POSTER = 'P'
        MISC ='M'
        
        
        
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=100)
    sold = models.fields.BooleanField(default=False)
    year= models.fields.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2027)], null=True)
    type = models.fields.CharField(choices=listingType.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)