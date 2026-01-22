from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# See all sold items
class SoldManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.SOLD)
 )

# See all for sale items
class SaleManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.FOR_SALE)
 )

# Seller Post
class Post(models.Model):
    class Status(models.TextChoices):
        SOLD = 'SD', 'Sold'
        FOR_SALE = 'FS', 'For Sale'
        
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    description = models.TextField()
    posted = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.FOR_SALE
    )
    objects = models.Manager() # The default manager.

    # Custom Managers
    sold = SoldManager()
    sale = SaleManager()

    class Meta:
        ordering = ['-posted']
        indexes = [
            models.Index(fields=['-posted'])
        ]
        
    def __str__(self):
        return self.name
    
