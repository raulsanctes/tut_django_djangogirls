from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    # on_delete=models.CASCADE (si se elimina el autor ¿se borra todo el
    # contenido de las propiedades
    # o sea, se borra título, texto, fecha de creación, publicación?
    autor = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # acá me hice una ensalada, pero entendí que si el campo de fecha de
    # publicación es blank=true EL CAMPO NO ES OBLIGATORIO y si
    # null=True ADEMÁS EL CAMPO SE ALMACENARÁ EN LA DB COMO NULL
    published_date = models.DateTimeField(blank=True, null=True)

    # no entendí mucho, solo que acá se crea la acción de publicar y guardarlo
    # con la fecha de la zona horaria colocada en settings.py
    # y devuelve el título del post.

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title