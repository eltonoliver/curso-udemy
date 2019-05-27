from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),
    )
    titulo = models.CharField(max_length=250)
    slug   = models.SlugField(max_length=250)#https://site.com/noticias/campeonato-brasileiro-2020/01/02/2020
    autor  = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    conteudo  = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado    = models.DateTimeField(auto_now_add=True)
    alterado  = models.DateTimeField(auto_now=True)
    status    = models.CharField(max_length=10,
                                 choices=STATUS,
                                 default='rascunho')

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo


# Create your models here.


"""
Post.objects.bulk_create([
    Post(titulo='Testando o shell do Django 2 com bulk',slug='testando-o-shell-do-django-22',conteudo='Testando o shell do Django',autor=user),
    Post(titulo='Testando o shell do Django 2 com bulk 2',slug='testando-o-shell-do-django-222',conteudo='Testando o shell do Django',autor=user),
    Post(titulo='Testando o shell do Django 2 com bulk 4',slug='testando-o-shell-do-django-2224',conteudo='Testando o shell do Django',autor=user),
])
"""