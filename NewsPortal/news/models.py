from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def get_username(self):
        return

    def update_rating(self, posts_rate, comments_rate, comments_posts_rate):
        self.rating = posts_rate * 3 + comments_rate + comments_posts_rate
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)


type_of_posts_choice = [
    ('ST', 'статья'),
    ('NE', 'новость')
]


class Post(models.Model):
    article = 'ST'
    news = 'NW'

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    type_of_post = models.CharField(max_length=2, choices=type_of_posts_choice)
    time_of_publication = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    header = models.CharField(max_length=255)
    text = models.TextField()
    rate = models.IntegerField(default=0)

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()

    def preview(self):
        try:
            preview_text = self.text[0:124] + '...'
        except IndexError:
            preview_text = self.text
        return preview_text

    def __str__(self):
        return f"{self.header}\n{self.text}\nАвтор: {self.user}"


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_of_public = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(default=0)

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()
