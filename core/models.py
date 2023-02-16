from django.db import models
from stdimage.models import StdImageField

from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
  criado = models.DateField("Data de criação", auto_now_add=True)
  modificado = models.DateField("Data de atualização", auto_now_add=True)
  ativo = models.BooleanField("Ativo?", default=True)

  class Meta:
    abstract = True

class Produto(Base):
  name = models.CharField("Nome", max_length=50)
  price = models.DecimalField("Preço", max_digits=8, decimal_places=2)
  thumbnail = StdImageField("Imagem", upload_to='produtos', variations={'thumb': (124, 124)}) # variations cria uma cópia da imagem com as especificações dadas
  slug = models.SlugField("Slug", max_length=100, blank=True, editable=False)

  def __str__(self):
    return self.name

def produto_pre_save(signal, instance, sender, **kwargs):
  instance.slug = slugify(instance.name)

signals.pre_save.connect(produto_pre_save, sender=Produto)