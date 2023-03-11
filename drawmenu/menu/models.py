from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):

    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )

    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name='children'
                            )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='URL'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )

    slug = models.SlugField(
        max_length=150,
        verbose_name='URL'
    )

    category = TreeForeignKey('Category',
                              on_delete=models.PROTECT,
                              related_name='posts',
                              verbose_name='Категория'
                              )

    content = models.TextField(verbose_name='Содержание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})