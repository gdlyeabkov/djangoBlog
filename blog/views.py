from .models import Rubric
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import *

class Home(ListView):
    template_name="blog/index.html"
    context_object_name= "posts"
    paginate_by = 2
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']="classic blog design"
        return context
def index(request):
    return render(request,"blog/index.html")

    def get_category(request,slug):
        return render(request, "blog/category.html")
    # return HttpResponse("<h1>привет мир</h1>")
# Create your views here.
class PostsByCategory(ListView):
    template_name = 'blog/index.html'
    allow_empty = True
    paginate_by=1
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']=Category.objects.get(slug=self.kwargs['slug'])
        return context
class GetPost(DetailView):
    model=Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.objects.views=F('views')+
        self.object.save()
        self.object.refresh_from_db()

        return context
class PostByTag(ListView):
    template_name='blog/index.html'
    allow_empty = True
    paginate_by=1
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='записи по тегу: ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context
class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 1
    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['s']=f's={self.request.GET.get('s')}&'
        return context
#------------------------------TestApp
def test(request):
    # return render(request,'\test.html')
    return render(request, "\test.html", {'rubrics': Rubric.objects.all()})
def get_rubric():
    pass
