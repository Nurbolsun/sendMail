from django.db import models

# Create your models here.


class Contact(models.Model):
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='Почта')
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name='Адрес')
    number_1 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Номер телефона')
    number_2 = models.CharField(max_length=100, blank=True, null=True, verbose_name='Резервный номер телефона')
    inn = models.CharField(max_length=100, blank=True, null=True, verbose_name='ИНН')
    gos_num = models.CharField(max_length=100, blank=True, null=True, verbose_name='ОГРН')

    def __str__(self):
        return self.email
