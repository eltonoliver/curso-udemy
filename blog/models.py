from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                           .filter(status='publicado')

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

    objects   = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo


# Create your models here.