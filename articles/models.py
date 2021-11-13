from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


def article_pre_save(sender, instance, *args, **kwargs):
    print("pre_save")

    if instance.slug is None:

        instance.slug = slugify(instance.title)

    # print(sender,instance,args, kwargs)


pre_save.connect(article_pre_save, sender=Articles)


def article_post_save(sender, instance, created, *args, **kwargs):
    print("post_save")

    if created:
        isinstance.slug = slugify(instance.title)
        isinstance.save()


post_save.connect(article_post_save, sender=Articles)
