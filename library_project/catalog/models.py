from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия", null=True, blank=True)
    date_birthd = models.DateField(verbose_name="Дата рождения", null=True, blank=True)

    def full_name(self):
        author = f"{self.name} {self.surname}"
        return author

    def __str__(self):
        author = f"{self.name} {self.surname}"
        return author

    class Meta:
        verbose_name_plural = "Авторы"
        verbose_name = "Автор"
        ordering = ["name"]


@receiver(post_save, sender=User)
def create_user_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_author(sender, instance, **kwargs):
    instance.author.save()


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    published = models.DateField(verbose_name="Дата публикации", null=True, blank=True)

    def __str__(self):
        book = f"{self.title}: {self.author}"
        return book

    class Meta:
        verbose_name_plural = "Книги"
        verbose_name = "Книга"
        ordering = ["title"]
