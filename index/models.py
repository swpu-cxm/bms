from django.db import models


# Create your models here.
class Publisher(models.Model):
    """
    出版社数据模型,包含ID和出版社名
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)


class Book(models.Model):
    """
    书籍数据模型,包含ID和书名,
    通过外键来存储出版社信息,为一对一关系,
    书籍和作者可以为多对多关系,所以和作者关系为ManyToMany
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publisher = models.ForeignKey(to='Publisher', on_delete=models.CASCADE)
    author = models.ManyToManyField(to='Author')


class Author(models.Model):
    """
    作者数据模型,包含ID和作者名
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    # book = models.ManyToManyField(to='Book')


