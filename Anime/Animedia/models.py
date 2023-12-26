from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=100)
    studios = models.ForeignKey('Animedia.Studio', on_delete=models.CASCADE)
    genres = models.ManyToManyField('Animedia.Genre')

    def __str__(self):
        return f"{self.id} {self.title}"

class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.genre}"
    
class Studio(models.Model):
    studio_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id} {self.studio_name}"
    
