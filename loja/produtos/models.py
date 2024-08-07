from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Categoria(models.Model):
    nome = models.CharField(max_length=32, unique=True)
    imagem = models.ImageField(upload_to="img_categoria/", blank=True, null=True)

    def __str__(self):
        return f"{self.nome}"


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=128)
    tamanho = models.CharField(max_length=10)
    nome = models.SlugField(max_length=512)
    valor = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    criado_em = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to="img/")
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    TAMANHO_CAMISA_CHOICES = [
        ("P", "Pequeno"),
        ("M", "Médio"),
        ("G", "Grande"),
        ("GG", "Extra Grande"),
    ]
    tamanho_camisa = models.CharField(
        max_length=2, choices=TAMANHO_CAMISA_CHOICES, null=True, blank=True
    )

    TAMANHO_CALCADO_CHOICES = [
        ("35", "35"),
        ("36", "36"),
        ("37", "37"),
        ("38", "38"),
        ("39", "39"),
        ("40", "40"),
        ("41", "41"),
        ("42", "42"),
        ("43", "43"),
        ("44", "44"),
    ]
    tamanho_calcado = models.CharField(
        max_length=2, choices=TAMANHO_CALCADO_CHOICES, null=True, blank=True
    )

    TAMANHO_ACESSORIO_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    tamanho_acessorio = models.CharField(
        max_length=2, choices=TAMANHO_ACESSORIO_CHOICES, null=True, blank=True
    )

    def __str__(self):
        return f"{self.descricao} ({self.categoria})"

    def get_absolute_url(self):
        return reverse("produto:categoria", args=(self.slug,))

    active = models.BooleanField(default=True)


class Carrinho(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through="CarrinhoItem")

    def __str__(self):
        produtos = [item.descricao for item in self.produtos.all()]
        return f"{self.user.id}: ({produtos})"


class CarrinhoItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    @property
    def total_item(self):
        return self.quantidade * self.produto.valor
