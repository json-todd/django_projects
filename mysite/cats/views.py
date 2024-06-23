from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Breed, Cat

# Create your views here.


class CatView(LoginRequiredMixin, View):
    def get(self, request):
        breed_count = Breed.objects.all().count()
        cat_list = Cat.objects.all()
        
        ctx = {'breed_count': breed_count, 'cat_list': cat_list}
        return render(request, 'cats/cat_list.html', context=ctx)
    
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    # On successful form submit, redirect user to the url whose path's name is "all" in the Cats app
    success_url = reverse_lazy('cats:all')
    
class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_urls = reverse_lazy('cats:all')

class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        breed_list = Breed.objects.all().count()
        ctx = {'breed_list': breed_list}
        return render(request,'cats/breed_list.html', context=ctx)
    
class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = 'cats:breed_view'
    
class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = 'cats:breed_view'
    
class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = 'cats:breed_view'
