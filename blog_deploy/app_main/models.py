from django.db import models
from django.core.validators import MinLengthValidator as MinVal

# Create your models here.


class Author(models.Model):
    frist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    #https://docs.djangoproject.com/en/5.0/ref/models/fields/#emailfield
    emial = models.EmailField()

    def full_name(self):
        return f"{self.frist_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.ImageField(upload_to="posts", null=True)

    #https://docs.djangoproject.com/en/5.0/ref/models/fields/#datefield
    date = models.DateField(auto_now=True)

    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinVal(10)])  #For large text

    #One-to-many relation
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    #SET_NULL :: If the author is deleted the author field shows NULL

    #Many-to-many relation
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField(max_length=120)
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.user_name} - {self.text}"


#
