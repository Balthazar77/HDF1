from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Brand(models.Model):
    """Бренд"""
    name = models.CharField(max_length=50, verbose_name="Бренд")
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренд'


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименнование категории')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, blank=True, verbose_name='URL')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Выберите категорию')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименования продукта')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Бренд", null=True)
    slug = models.SlugField(max_length=200, db_index=True, blank=True, verbose_name='URL')
    image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    articul = models.SlugField(unique=True, max_length=20, null=True)
    stock = models.PositiveIntegerField(verbose_name='Количество')
    available = models.BooleanField(default=True, verbose_name='В наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    analog = models.CharField(max_length=255, verbose_name='Аналог', null=True)
    applicability = models.CharField(max_length=255, verbose_name='Применение', null=True)
    filter_weight = models.FloatField(default=0, verbose_name='Вес')
    filter_volume = models.FloatField(default=0, verbose_name='Объем')
    filter_size = models.CharField(max_length=255, verbose_name='Размер',null=True)


    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
