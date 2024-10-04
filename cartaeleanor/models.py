from django.db import models

class Index(models.Model):
    # Seção 1
    secao1_imagemFundo = models.ImageField(upload_to='cartaeleanor', blank=True)
    secao1_imagemAutor = models.ImageField(upload_to='cartaeleanor', blank=True)
    secao1_titulo1 = models.CharField(max_length=150)
    secao1_titulo2 = models.CharField(max_length=150)
    secao1_descricao = models.TextField()

    # Seção 2
    secao2_imagemFundo = models.ImageField(upload_to='cartaeleanor', blank=True)
    secao2_titulo = models.CharField(max_length=150)
    secao2_texto = models.TextField()

    # Seção 3
    secao3_titulo = models.CharField(max_length=150)

    leitor1_imagem = models.ImageField(upload_to='cartaeleanor', blank=True)
    leitor1_texto = models.TextField()
    leitor1_nome = models.CharField(max_length=150)

    leitor2_imagem = models.ImageField(upload_to='cartaeleanor', blank=True)
    leitor2_texto = models.TextField()
    leitor2_nome = models.CharField(max_length=150)

    leitor3_imagem = models.ImageField(upload_to='cartaeleanor', blank=True)
    leitor3_texto = models.TextField()
    leitor3_nome = models.CharField(max_length=150)

    leitor4_imagem = models.ImageField(upload_to='cartaeleanor', blank=True)
    leitor4_texto = models.TextField()
    leitor4_nome = models.CharField(max_length=150)

    leitor5_imagem = models.ImageField(upload_to='cartaeleanor', blank=True)
    leitor5_texto = models.TextField()
    leitor5_nome = models.CharField(max_length=150)

    # Seção 4
    secao4_titulo = models.CharField(max_length=150)
    secao4_texto = models.TextField()
    secao4_imagem1 = models.ImageField(upload_to='cartaeleanor', blank=True)
    secao4_imagem2 = models.ImageField(upload_to='cartaeleanor', blank=True)

    # Seção 5
    secao5_texto = models.TextField()
    secao5_botao = models.CharField(max_length=150)
    secao5_imagemFundo = models.ImageField(upload_to='cartaeleanor', blank=True)