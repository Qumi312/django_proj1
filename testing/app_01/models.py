from ipaddress import ip_address
from tabnanny import verbose
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class Logg(models.Model):
    address_ip = models.CharField(max_length=15, verbose_name ="IP-адрес")
    date = models.CharField(max_length=20, verbose_name = "Дата")
    method = models.CharField(max_length=20, verbose_name = 'Метод запроса')
    url = models.CharField(max_length=40, verbose_name = 'URL_запроса')
    answer = models.IntegerField(verbose_name = 'Код ответа')
    answer_size = models.IntegerField(verbose_name = "Размер ответа")

    class Meta:
        db_table = "logging"
        verbose_name = "Результат логгирования"
        
    def __str__(self):
        return self.address_ip

class UploadFiles(models.Model):
    file = models.FileField(upload_to='files/')