from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
    "Model for genre of Book"
    name = models.CharField(max_length=100, help_text='The Description of the book')

    def __str__(self):
        "The String for representing the Book model"
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=100, help_text='Enter the summary of the book')
    isbn = models.CharField('isbn',max_length=13,help_text='The isbn of the book')

    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique id for a book')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=100)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m','Maintanance'),
        ('o', 'On loan'),
        ('a','Available'),
        ('r','Reversed'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book Availbality',
    )
    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    date_of_death = models.DateField(
        'Died',
        null=True,
        blank=True,
    )
    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'