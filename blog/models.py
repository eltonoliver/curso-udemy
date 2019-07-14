from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                           .filter(status='publicado')

class Category(models.Model):
    nome = models.CharField(max_length=100)
    publicado = models.DateTimeField(default=timezone.now)
    criado    = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-criado']

    def __str__(self):
        return self.nome

class Post(models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),
    )
    titulo = models.CharField(verbose_name="Título",max_length=250)
    slug   = models.SlugField(max_length=250)
    autor  = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Category, related_name="get_posts")
    imagem    = models.ImageField(upload_to="blog",blank=True, null=True)
    conteudo  = RichTextField(verbose_name="Conteúdo")
    publicado = models.DateTimeField(default=timezone.now)
    criado    = models.DateTimeField(auto_now_add=True)
    alterado  = models.DateTimeField(auto_now=True)
    status    = models.CharField(max_length=10,
                                 choices=STATUS,
                                 default='rascunho')

    objects   = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.slug])

    def get_absolute_url_update(self):
        return reverse('post_edit',args=[self.pk])
    @property
    def view_image(self):
        return mark_safe('<img src="%s" width="400px" />'%self.imagem.url)   
        view_image.short_description = "Imagem Cadastrada" 
        view_image.allow_tags = True    

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo

    

@receiver(post_save,sender=Post)
def insert_slug(sender,instance,**kwargs):
    if kwargs.get('created',False):
        print('Criando slug')
    if not instance.slug:
        instance.slug = slugify(instance.titulo)
        return instance.save()

# Create your models here.
