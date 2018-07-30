from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
# Create your views here.

from .models import Item
from .forms import ItemForm


class HomeView(View):
    def get(self, request, **kwargs):
        if not request.user.is_authenticated():
            return render(request, 'home.html', {})
        user = request.user
        is_following_user_ids = [x.user.id for x in user.is_following.all()]
        qs = Item.objects.filter(user__id__in=is_following_user_ids, public=True)
        return render(request, 'menus/home-feed.html', {'object_list': qs})


class ItemListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetailView(LoginRequiredMixin, DetailView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(LoginRequiredMixin, CreateView):
    form_class = ItemForm
    template_name = 'form.html'

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ItemCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Add Item'
        return context


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ItemForm
    template_name = 'form.html'

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update Item'
        return context

    def get_form_kwargs(self):
        kwargs = super(ItemUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
