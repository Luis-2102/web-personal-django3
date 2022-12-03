from django.db import models

# Create your models here.
class Proyect(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Título')
    description = models.TextField(verbose_name = 'Descripción')
    image = models.ImageField(verbose_name = 'Imagen', upload_to= "proyects")
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de Creación')
    update = models.DateField(auto_now=True, verbose_name = 'Fecha de Actualizacion')
    URLField = models.URLField(null=True, blank=True)

    
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = [ "-created" ]
        def __str__(self):
            return self.title
