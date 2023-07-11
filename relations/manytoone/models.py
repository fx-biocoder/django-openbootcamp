from django.db import models

# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.email 
    

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publication_date = models.DateField(auto_now_add=True)
    # ¿La siguiente línea de código representa adecuadamente una relación muchos a uno? (muchos articulos, un redactor)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.headline