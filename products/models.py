from django.db import models

# Create your models here.
'''
Описание продуктовой группы
'''
class ProductGroup(models.Model):
    class Meta:
        verbose_name = 'Группа продуктов'
        verbose_name_plural = 'Группы продуктов'

    name = models.CharField(
        max_length=100,
        verbose_name='Наименование группы',
    )

    description = models.CharField(
        max_length=400,
        verbose_name='Описание',
    )

    def __str__(self):
        return self.name


'''
Описание продукта
'''
class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    name = models.CharField(
        max_length=100,
        verbose_name='Наименование продукта',
    )

    description = models.CharField(
        max_length=400,
        verbose_name='Описание продукта',
        blank=True,
    )

    product_group = models.ForeignKey(
        ProductGroup,
        on_delete=models.SET_NULL,
        verbose_name='Продуктовая группа',
        null=True,
    ) 


    def __str__(self):
        return self.name





