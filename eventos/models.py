from ast import Bytes
from email.policy import default
from statistics import mode
from tokenize import blank_re
from turtle import up
from django.db import models
from django.urls import reverse
from io import BytesIO
import qrcode
from django.core.files import File
from PIL import Image, ImageDraw

class Evento(models.Model):
    nombre  = models.CharField(max_length = 200)
    artista = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 500, default=None)
    fecha = models.CharField(max_length=50, blank=False, null=True)
    precio = models.FloatField(null=True, blank=True)
    lugar = models.CharField(max_length = 200, blank=False, null=True)
    image_url = models.CharField(max_length = 2083, default=False)
    ver_instragram = models.CharField(max_length=2083, blank=True)  
    evento_valido = models.BooleanField(default=False)
    #code = models.ImageField(blank=True, upload_to='code', null= False)
    codigoqr = models.CharField(max_length = 2083, default=False)

    def __str__(self):
        return self.nombre
    
    #def save(self, *args, **kwargs):
    #    qr_image = qrcode.make(self.nombre)
    #    qr_offset = Image.new('RGB', (310, 310), 'white')
    #    qr_offset.paste(qr_image)
    #    files_name = f'{self.nombre}-{self.id}qr.png'
    #    stream = BytesIO()
    #    qr_offset.save(stream, 'PNG')
    #    self.code.save(files_name, File(stream), save=False)
    #    qr_offset.close()
    #    super().save('*args, **kwargs')
    


class Orden(models.Model):
	product = models.ForeignKey(Evento, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.nombre