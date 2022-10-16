from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.models import Auto, Make
from autos.forms import MakeForm, AutoForm

# =================== MAIN VIEW ===========================

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        make_count = Make.objects.all().count()
        auto_list = Auto.objects.all()

        ctx = {'make_count': make_count, 'auto_list': auto_list}
        return render(request, 'autos/auto_list.html', ctx)

# =================== END MAIN VIEW ===========================

# =================== MAKE VIEWS ===========================

class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        make_list = Make.objects.all()
        ctx  = {'make_list': make_list}
        return render(request, 'autos/make_list.html', ctx)


class MakeCreate(LoginRequiredMixin, View):
    form_template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:all')

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

"""
class MakeView(LoginRequiredMixin, Createview):
    model = Make
    field = '__all__'
    success_url = reverse_lazy('autos:all')
"""

class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy('autos:all')
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


"""
class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
"""

class MakeDelete(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy('autos:all')
    delete_template = 'autos/make_confirm_delete.html'

    def get(self, request, pk):
        make_object = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make_object)
        ctx = {'form': form}
        return render(request, self.delete_template, ctx)

    def post(self, request, pk):
        make_object = get_object_or_404(self.model, pk=pk)
        make_object.delete()
        return redirect(self.success_url)

"""
class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
"""
# =================== END MAKE VIEWS ===========================

# =================== AUTO VIEWS ===========================

class AutoCreate(LoginRequiredMixin, View):
    model = Auto
    # fields = '__all__'
    success_url = reverse_lazy('autos:all')
    form_template = 'autos/auto_form.html'

    def get(self, request):
        form = AutoForm()
        ctx = {'form': form}
        return render(request, self.form_template, ctx)

    def post(self, request):
        form = AutoForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.form_template, ctx)
        else:
            form.save()
            return redirect(self.success_url)


class AutoUpdate(LoginRequiredMixin, View):
    model = Auto
    # fields = '__all__'
    success_url = reverse_lazy('autos:all')
    form_template = 'autos/auto_form.html'

    def get(self, request, pk):
        auto_object = get_object_or_404(self.model, pk=pk)
        form = AutoForm(instance=auto_object)
        ctx = {'form': form}
        return render(request, self.form_template, ctx)

    def post(self, request, pk):
        auto_object = get_object_or_404(self.model, pk=pk)
        form = AutoForm(request.POST, instance=auto_object)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.form_template, ctx)
        else:
            form.save()
            return redirect(self.success_url)

class AutoDelete(LoginRequiredMixin, View):
    model = Auto
    # fields = '__all__'
    success_url = reverse_lazy('autos:all')
    delete_template = 'autos/auto_confirm_delete.html'

    def get(self, request, pk):
        auto_object = get_object_or_404(self.model, pk=pk)
        form = AutoForm(instance=auto_object)
        ctx = {'form': form}
        return render(request, self.delete_template, ctx)

    def post(self, request, pk):
        auto_object = get_object_or_404(self.model, pk=pk)
        auto_object.delete()
        return redirect(self.success_url)












