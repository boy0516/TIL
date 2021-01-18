from django.db import models

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    stock_quantity = models.CharField(max_length=100)
    description = models.TextField()

class Comment(models.Model):
    Post = models.ForeignKey('product.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
    def __str__(self):
        return self.text


# Create your models here.
