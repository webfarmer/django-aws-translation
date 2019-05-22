# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from django.db import models
from translatable.models import get_translation_model, TranslatableModel
fs = FileSystemStorage(location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL)

STATUS_CHOICES = (
    ("draft", "Draft",),
    ("live", "Live / Published",),
)

class Page(TranslatableModel):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(max_length=150,blank=False, null=False)
    display = models.BooleanField(default=True)
    status = models.CharField(max_length=34, choices=STATUS_CHOICES, default="draft")
    published_date = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"


class PageTranslation(get_translation_model(Page, "page")):
    title = models.CharField(max_length=150, blank=False, null=False)
    subtitle = models.CharField(max_length=150, blank=False, null=False)
    slug =  models.SlugField(max_length=150,blank=False, null=False)
    content = models.TextField(blank=False, null=False)

    meta_title = models.CharField("Title",max_length=255, null=True, blank=True)
    meta_description = models.CharField("Description",max_length=255, null=True, blank=True)
    meta_keywords = models.CharField("Keywords",max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.model.name

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"


class MailChimpList(models.Model):
    list_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)


class Newsletter(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    mailchimp_list = models.ManyToManyField(MailChimpList, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)


def get_blog_image_path(self, filename):
    return "/media/blog/%s" % filename.replace("(", "").replace(")", "")


class TroubleShooting(TranslatableModel):
    DEVICE_CHOICES = (
        ("hero-se", "Snuza Hero SE"),
        ("pico", "Snuza Pico"),
        ("hero-md", "Snuza Hero MD"),
        ("go", "Snuza Go"),
    )
    slug = models.SlugField(max_length=255)
    display = models.BooleanField()
    device = models.CharField(choices=DEVICE_CHOICES, max_length=255)
    order = models.IntegerField(default=0)
    status = models.CharField(max_length=34, choices=STATUS_CHOICES, default="draft")
    published_date = models.DateTimeField(blank=True, null=True)


    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)


class TroubleShootingTranslation(get_translation_model(TroubleShooting, "troubleshooting")):
    question = models.CharField(max_length=255)
    answer = models.TextField()


class BabyTimes(TranslatableModel):
    TIMES_CHOICES = (
        ("testimonial", "Testimonial"),
        ("review", "Review"),
    )
    slug = models.SlugField(max_length=255)
    display = models.BooleanField(default=True)
    times_type = models.CharField(choices=TIMES_CHOICES, max_length=255)
    order = models.IntegerField(default=0)
    status = models.CharField(max_length=34, choices=STATUS_CHOICES, default="draft")
    published_date = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "Baby Times"
        verbose_name_plural = "Baby Times"


class BabyTimesTranslation(get_translation_model(BabyTimes, "babytimes")):
    title = models.CharField(max_length=255)
    timestamp = models.DateField()
    content = models.TextField()


class Certification(TranslatableModel):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to="certifications/", blank=True, null=True)
    order = models.IntegerField(default=0)
    display = models.BooleanField()
    status = models.CharField(max_length=34, choices=STATUS_CHOICES, default="draft")
    published_date = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order"]


class CertificationTranslation(get_translation_model(Certification, "certification")):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class Category(TranslatableModel):
    slug = models.SlugField(max_length=255)
    display = models.BooleanField()
    order = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)


class CategoryTranslation(get_translation_model(Category, "Category")):
    title = models.CharField(max_length=255)


class BlogArticle(TranslatableModel):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(max_length=150,blank=False, null=False)
    status = models.CharField(max_length=34, choices=STATUS_CHOICES, default="draft")
    published_date = models.DateTimeField(blank=True, null=True)

    display = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True)
    image = models.FileField(upload_to=get_blog_image_path, storage=fs, blank=False, null=False)

    order = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog Article"
        verbose_name_plural = "Blog Articles"


class BlogArticleComment(models.Model):
    article = models.ForeignKey(BlogArticle, on_delete=models.DO_NOTHING)

    language = models.CharField(choices=settings.LANGUAGES, max_length=14)

    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)


class BlogArticleTranslation(get_translation_model(BlogArticle, "blogarticle")):
    title = models.CharField(max_length=150, blank=False, null=False)
    short_description = models.TextField(blank=False, null=False)
    slug =  models.SlugField(max_length=150,blank=False, null=False)
    content = models.TextField(blank=False, null=False)

    meta_title = models.CharField("Title",max_length=255, null=True, blank=True)
    meta_description = models.CharField("Description",max_length=255, null=True, blank=True)
    meta_keywords = models.CharField("Keywords",max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now = True)
    modified_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.model.name

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

