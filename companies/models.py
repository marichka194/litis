#  -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=180, verbose_name=u"Название категории")
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Категория"
        verbose_name_plural = u"Категории"

class SubCategory(models.Model):
    name = models.CharField(max_length=180, verbose_name=u"Название подкатегории")
    category = models.ForeignKey(Category, verbose_name=u"Категория")
    def __unicode__(self):
        return self.category.name + " : " + self.name

    class Meta:
        verbose_name = u"Подкатегория"
        verbose_name_plural = u"Подкатегории"

class Company(models.Model):
    name = models.CharField(max_length=180, verbose_name=u"Имя компании")
    address = models.TextField(verbose_name=u"Адрес компании")
    description = models.TextField(verbose_name=u"Описание")
    rating = models.IntegerField(verbose_name=u"Рейтинг", default=0)
    image = models.ImageField(upload_to="logo", verbose_name=u"Логотип", null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, verbose_name=u"Подкатегория")
    on_map = models.TextField(verbose_name=u"Код отображения карты", default=" ", blank=True)


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["rating", "name"]
        verbose_name = u"Компания"
        verbose_name_plural = u"Компании"