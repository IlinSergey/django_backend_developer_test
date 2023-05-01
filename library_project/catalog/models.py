from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    date_birthd = models.DateField(verbose_name="Дата рождения")

    def __str__(self):
        author = f"{self.name} {self.surname}"
        return author

    class Meta:
        verbose_name_plural = "Авторы"
        verbose_name = "Автор"
        ordering = ["name"]


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    published = models.DateField(verbose_name="Дата публикации")

    def __str__(self):
        book = f"{self.title}: {self.author}"
        return book

    class Meta:
        verbose_name_plural = "Книги"
        verbose_name = "Книга"
        ordering = ["title"]
