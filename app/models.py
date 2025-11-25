from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True )
    title = models.CharField(max_length=122)
    description = models.TextField(null=True)
    date = models.DateTimeField(auto_created="now")
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.title

