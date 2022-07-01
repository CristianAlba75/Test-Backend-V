from django.db import models

# Create your models here.


class Post(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False, unique=True, blank=False,
        verbose_name="id",
        help_text="ID Post"
    )
    created_at = models.DateField(
        null=False, blank=False, auto_now_add=True,
        verbose_name="created AT",
        help_text="Date Post Created"
    )
    name = models.CharField(
        null=False, unique=True, blank=False,
        max_length=200,
        verbose_name="title",
        help_text="Name Post"
    )
    content = models.TextField(
        null=False, blank=False,
        verbose_name="content",
        help_text="Content Post"
    )
    email = models.CharField(
        null=False, blank=False,
        max_length=255,
        verbose_name="email",
        help_text="email owner Post"
    )
    likes = models.PositiveIntegerField(
        null=True, blank=True, default=0,
        verbose_name="likes",
        help_text="likes Post"
    )
    dislikes = models.PositiveIntegerField(
        null=True, blank=True, default=0,
        verbose_name="dislikes",
        help_text="dislikes Post"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
