from django.db import models
from products.models import Product
from products.models import ProductGroup
from geo.models import Position


# Create your models here.

class Supplier(models.Model):
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    name = models.CharField(
        max_length=300,
        verbose_name='ФИО',
    )    

    phone = models.CharField(
        max_length=200,
        verbose_name='Телефон',
    )

    address = models.CharField(
        max_length=500,
        verbose_name='Адрес',
        default='',
        blank=True,
    )

    raiting = models.IntegerField(
        verbose_name='Рейтинг',
        default=0,
    )
    
    comments = models.CharField(
        max_length=500,
        blank=True,
        verbose_name='Комментарии',
    )

    def __str__(self):
        return self.name


class Feedback(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    rate = models.IntegerField(
        default=0,
        verbose_name='Рейтинг',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete = models.CASCADE,
    )

    comments = models.CharField(
        max_length=500,
        verbose_name='Комментарии',
        blank= True,
    )

    def __str__(self):
        return "%s - %d"%(self.name, self.rate)


class Point(models.Model):
    class Meta:
        verbose_name = "Точка продаж"
        verbose_name_plural = "Точки продаж"

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name = 'Поставщик',
    )    

    position = models.ForeignKey(
        Position,
        null = True,
        on_delete=models.SET_NULL,
        verbose_name = 'Адрес'
    )

    product = models.ManyToManyField(
        Product,
        verbose_name='Продукт',

    )
