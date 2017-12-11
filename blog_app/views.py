# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        """do form authentication and login in user. redirect to homepage"""
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('post-list')


        # return render(request, 'registration/signup.html', {'form': form})
    else:
        """open signup form"""
        form = UserCreationForm()

        context = {'form': form}
    return render(request, 'registration/signup.html', context)


class BlogListView(ListView):
    model = Post
    template_name = 'blog/index.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'


class BlogCreateView(CreateView):
    model = Post
    # fields = '__all__'
    template_name = 'blog/post_new.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BlogCreateView, self).form_valid(form)


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'text']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post-list')
