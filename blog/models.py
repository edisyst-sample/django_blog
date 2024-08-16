from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User


class Tag(models.Model):
    """
    Modello per rappresentare i tag associati ai post.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Modello per rappresentare un post del blog.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title


# Funzione per creare dati fake
def create_fake_posts(n=5):
    fake = Faker()
    for _ in range(n):
        Post.objects.create(
            title=fake.sentence(),
            content=fake.paragraph(),
        )


class Comment(models.Model):
    """
    Modello per rappresentare un commento su un post del blog.
    """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"




