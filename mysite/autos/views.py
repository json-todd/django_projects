from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.models import Auto, Make
from autos.forms import MakeForm

class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        make_list = Make.objects.all()
        ctx  = {'make_list': make_list}
        return render(request, 'autos/make_list.html', ctx)

class MakeCreate(LoginRequiredMixin, View):
    form_template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:make_list')

    def get(self, request):
        form = MakeForm()
        ctx = {'form': form}
        return render(request, self.form_template, ctx)

    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.form_template, ctx)
        else:
            form.save()
            return redirect(self.success_url)

class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy('autos:make_list')
    form_template = 'autos/make_form.html'

    def get(self, request, pk):
        make_object = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make_object)
        ctx = {'form': form}
        return render(request, self.form_template, ctx)

    def post(self, request, pk):
        make_object = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance = make_object)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.form_template, ctx)
        else:
            form.save()
            return redirect(self.success_url)

class MakeDelete(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy('autos:make_list')
    form_template = 'autos/make_form.html'

    def get(self, request, pk):
        make_object = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make_object)
        ctx = {'form': form}
        return render(request, self.form_template, ctx)

    def post(self, request, pk):
        make_object = get_object_or_404(self.model, pk=pk)
        make_object.delete()
        return redirect(self.success_url)

class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')