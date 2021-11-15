import random
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.http.response import HttpResponseRedirect
from django.utils import timezone
from .utils import slugify_instance_title
from django.db.models import Q, lookups
####
from django.urls import reverse
from django.conf import settings
# Create your models here.
# new

user = settings.AUTH_USER_MODEL


class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)


# new
class ArticleManger(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query=None):

        return self.get_queryset().search(query=query)

# defult


class Articles(models.Model):
    user = models.ForeignKey(
        user, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)

    objects = ArticleManger()

    def save(self, *args, **kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # return f'/articles/{self.slug}/'

        return reverse('article-detail',  kwargs={'slug': self.slug})


# def slugify_instance_title(instance, save=False, new_slug=None):
#     if new_slug is not None:
#         slug = new_slug
#     else:
#         slug = slugify(instance.title)

#     qs = Articles.objects.filter(slug=slug).exclude(id=instance.id)
#     if qs.exists():
#         rand_int = random.randint(300_000, 500_000)
#         slug = f"{slug}-{rand_int}"
#         return slugify_instance_title(instance, save=False, new_slug=slug)
#     instance.slug = slug
#     if save:
#         instance.save
#     return instance


def article_pre_save(sender, instance, *args, **kwargs):
    print("pre_save")

    if instance.slug is None:
        slugify_instance_title(instance, save=False)

    # print(sender,instance,args, kwargs)


pre_save.connect(article_pre_save, sender=Articles)


def article_post_save(sender, instance, created, *args, **kwargs):
    print("post_save")

    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(article_post_save, sender=Articles)
