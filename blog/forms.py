from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post

class Postform(forms.ModelForm):
    titulo = forms.CharField(max_length=100)
    conteudo = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('titulo','conteudo','categoria','imagem','status')

   