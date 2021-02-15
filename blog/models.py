from django.db import models
from django.urls import reverse


class Category(models.Model):
    title=models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url' ,unique=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['title',]
class Tag(models.Model):
    title=models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url',unique=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('category',kwargs={"slug":self.slug})
    class Meta:
        ordering=['title',]
class Post(models.Model):
    title=models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url',unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    views = models.IntegerField(default=0,verbose_name='колво просмотов')
    category = models.ForeignKey(Category,on_delete=models.PROTECT, related_name="posts")
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post',kwargs={"slug":self.slug})
    class Meta:
        ordering=[-'created_at',]

# Create your models here.
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Rubric(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('rubric',kwargs={"slug":self.slug})
    class MPTTMeta:
        order_insertion_by = ['name']
class Article(models.Model):
    name=models.CharField(max_length=50)
    # category=models.ForeignKey(Rubric,on_delete=models.PROTECT())
    category = models.TreeForeignKey(Rubric, on_delete=models.PROTECT())
    def __str__(self):
        return self.name

