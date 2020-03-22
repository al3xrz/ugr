from django.db import models

'''
Муниципальное образование
'''
class Municipality(models.Model):

    class Meta:
        verbose_name = 'Муниципальное образование'
        verbose_name_plural = 'Муниципальные образования'
        ordering = ('name', )

    name = models.CharField(
        max_length=200,
        verbose_name='Муниципальное образование'
    )

    def __str__(self):
        return self.name


'''
Населенный пункт
'''
class Locality(models.Model):

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'
        ordering = ('name',)

    name = models.CharField(
        verbose_name='Населенный пункт',
        max_length=200
    )

    municipality = models.ForeignKey(
        Municipality,
        verbose_name='Муниципальное образование',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name



'''
Расположение точки
'''

class Position(models.Model):
    class Meta:
        verbose_name = 'Расположение'
        verbose_name_plural = 'Расположения'
    
    locality = models.ForeignKey(
        Locality,
        verbose_name = 'Населенный пункт',
        on_delete=models.SET_NULL,
        null = True,
    )
    
    address = models.CharField(
        max_length=500,
        verbose_name='Адрес',
    )

    lat = models.FloatField(
        verbose_name='Широта',
        blank = True,
    )

    lon = models.FloatField(
        verbose_name='Долгота',
        blank = True,
    )

    comments = models.CharField(
        max_length= 1000,
        verbose_name='Комментарии',
        blank=True,
    )

    def __str__(self):
        return "%s - %s"%(self.locality, self.address)

