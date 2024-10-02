from django.db import models

class Index(models.Model):
    # Seção 1
    secao1_imagemFundo = models.ImageField()
    secao1_imagemAutor = models.ImageField()
    secao1_titulo1 = models.CharField(max_length=150)
    secao1_titulo2 = models.CharField(max_length=150)
    secao1_descricao = models.TextField()

    # Seção 2
    secao2_imagemFundo = models.ImageField()
    secao2_titulo = models.CharField(max_length=150)
    secao2_texto = models.TextField()

    # Seção 3
    secao3_titulo = models.CharField(max_length=150)

    leitor1_imagem = models.ImageField()
    leitor1_texto = models.TextField()
    leitor1_nome = models.CharField(max_length=150)

    leitor2_imagem = models.ImageField()
    leitor2_texto = models.TextField()
    leitor2_nome = models.CharField(max_length=150)

    leitor3_imagem = models.ImageField()
    leitor3_texto = models.TextField()
    leitor3_nome = models.CharField(max_length=150)

    leitor4_imagem = models.ImageField()
    leitor4_texto = models.TextField()
    leitor4_nome = models.CharField(max_length=150)

    leitor5_imagem = models.ImageField()
    leitor5_texto = models.TextField()
    leitor5_nome = models.CharField(max_length=150)

    # Seção 4
    secao4_titulo = models.CharField(max_length=150)
    secao4_texto = models.TextField()
    secao4_imagem1 = models.ImageField()
    secao4_imagem2 = models.ImageField()

    # Seção 5
    secao5_texto = models.TextField()
    secao5_botao = models.CharField(max_length=150)
    secao5_imagemFundo = models.ImageField()