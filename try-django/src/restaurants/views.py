from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class RestaurantListView(LoginRequiredMixin, ListView):
    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)


class RestaurantDetailView(LoginRequiredMixin, DetailView):
    template_name = 'restaurants/restaurants_detail.html'

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)


def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/restaurants/')
    if form.errors:
        errors = form.errors
    template_name = 'restaurants/form.html'
    context = {'form': form, 'errors': errors}
    return render(request, template_name, context)


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Add Restaurant'
        return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update Restaurant'
        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)




