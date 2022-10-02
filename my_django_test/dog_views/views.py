
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
# Create your views here.


class OwnerCreateView(CreateView):
    model = Owner
    fields = "__all__"
    success_url = reverse_lazy("dog_views:list_owner")


class OwnerListView(ListView):
    model = Owner
    context_object_name = "owner_list"


class OwnerUpdateView(UpdateView):
    model = Owner
    fields = "__all__"
    success_url = reverse_lazy("dog_views:list_owner")


class OwnerDeleteView(DeleteView):
    model = Owner
    success_url = reverse_lazy("dog_views:list_owner")


class OwnerDetailView(DetailView):
    model = Owner


class DoggoUpdateView(UpdateView):
    model = Doggo
    fields = "__all__"
    success_url = reverse_lazy("dog_views:list_dog")


class DoggoDetailView(DetailView):
    model = Doggo


class DoggoListView(ListView):
    model = Doggo
    context_object_name = "dog_list"


class DoggoDeleteView(DeleteView):
    model = Doggo
    success_url = reverse_lazy("dog_views:list_dog")


class DoggoCreateView(CreateView):
    model = Doggo
    fields = "__all__"
    success_url = reverse_lazy("dog_views:list_dog")

