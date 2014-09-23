#  -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=180, verbose_name=u"Название категории")
    slug = models.SlugField()
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Категория"
        verbose_name_plural = u"Категории"


class SubCategory(models.Model):
    name = models.CharField(max_length=180, verbose_name=u"Название подкатегории")
    slug = models.SlugField()
    category = models.ForeignKey(Category, verbose_name=u"Категория")
    def __unicode__(self):
        return self.category.name + " : " + self.name

    class Meta:
        ordering = ['name']
        verbose_name = u"Подкатегория"
        verbose_name_plural = u"Подкатегории"


class Company(models.Model):
    name = models.CharField(max_length=180, verbose_name=u"Имя компании")
    meta_words = models.TextField(verbose_name=u"Ключевые слова", default=" ", blank=True)
    email = models.EmailField(verbose_name="E-mail", max_length=75)
    site = models.URLField(verbose_name=u"Персональный сайт", blank=True, help_text=u"(если есть)")
    phone = models.CharField(max_length=15, verbose_name=u"Телефон", blank=True)
    description = models.TextField(verbose_name=u"Описание", blank=True)
    recommendations = models.TextField(verbose_name=u"Пожелания и рекомендации", blank=True)
    person = models.CharField(max_length=100, verbose_name=u"Контактное лицо")
    rating = models.FloatField(verbose_name=u"Рейтинг", default=0, editable=False)
    voted = models.IntegerField(default=0, editable=False)
    sum_rating = models.IntegerField(default=0, editable=False)
    #voted_3 = models.IntegerField(default=0, editable=False)
    #voted_4 = models.IntegerField(default=0, editable=False)
    #voted_5 = models.IntegerField(default=0, editable=False)
    image = models.ImageField(upload_to="logo", verbose_name=u"Логотип", null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, verbose_name=u"Подкатегория")
    on_map = models.TextField(verbose_name=u"Код отображения карты", default=" ", blank=True)
    slug = models.SlugField()
    accepted = models.BooleanField(verbose_name=u"Подтверждение", default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-rating", "name"]
        verbose_name = u"Компания"
        verbose_name_plural = u"Компании"


class Address(models.Model):
    address = models.CharField(max_length=300, verbose_name=u"Адрес")
    company = models.ForeignKey(Company, verbose_name=u"Компания")
    def __unicode__(self):
        return self.address

    class Meta:
        verbose_name = u"Адрес"
        verbose_name_plural = u"Адреса"


class StoredSession(models.Model):
    session_id = models.CharField(max_length=50)
    company = models.ForeignKey(Company)



class SimplePage(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=250)
    page = models.TextField()
