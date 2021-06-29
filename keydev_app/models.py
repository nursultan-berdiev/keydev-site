from django.db import models

class Messages(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ф.И.О \ Наименование организации')
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=10, verbose_name='Номер телефона')
    message = models.TextField(verbose_name='Напишите нам сообщение')

    def __str__(self):
        return self.name
