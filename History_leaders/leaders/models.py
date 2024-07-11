from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
   
class Trait(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name    

class Leader(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    lifetime = models.CharField(max_length=100)
    achievements = models.TextField()
    wikipedia_link = models.URLField()
    image = models.ImageField(upload_to='leaders/')
    traits = models.ManyToManyField(Trait, blank= True)

    def __str__(self):
        return self.name
    






