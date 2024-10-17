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

class IndexText(models.Model):
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    text4 = models.TextField()
    text5 = models.TextField()
    text6 = models.TextField()
    text7 = models.TextField()
    text8 = models.TextField()
    text9 = models.TextField()
    text10 = models.TextField()
    text11 = models.TextField()
    text12 = models.TextField()
    text13 = models.TextField()
    text14 = models.TextField()
    text15 = models.TextField()
    text16 = models.TextField()
    text17 = models.TextField()
    text18 = models.TextField()
    text19 = models.TextField()
    text20 = models.TextField()

class IndexImage(models.Model):
    image1 = models.ImageField(upload_to='cartaeleanor', blank=True)
    image2 = models.ImageField(upload_to='cartaeleanor', blank=True)
    image3 = models.ImageField(upload_to='cartaeleanor', blank=True)
    image4 = models.ImageField(upload_to='cartaeleanor', blank=True)
    image5 = models.ImageField(upload_to='cartaeleanor', blank=True)
    image6 = models.ImageField(upload_to='cartaeleanor', blank=True)
    image7 = models.ImageField(upload_to='cartaeleanor', blank=True)
    image8 = models.ImageField(upload_to='cartaeleanor', blank=True)

class IndexBackground(models.Model):
    bg1 = models.ImageField(upload_to='cartaeleanor', blank=True)
    bg2 = models.ImageField(upload_to='cartaeleanor', blank=True);

class IndexPseudoImage(models.Model):
    pseudoimage1 = models.ImageField(upload_to='cartaeleanor', blank=True)