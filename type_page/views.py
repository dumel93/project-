from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import UserLoginForm, UserCreateForm

from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TyperBaseView(View):

    def get(self,request):
        return render(request, 'type_page/base.html')


class TyperIndexView(View):
    def get(self,request):
        form = UserLoginForm()
        ctx = {'form': form}
        return render(request, 'type_page/index.html', ctx)



class UserLoginView(View):

    def get(self, request):
        form = UserLoginForm()
        ctx = {'form': form}
        return render(
            request,
            'type_page/index.html',
            ctx
        )


    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('index/')
        else:
            return render(
                request,
                'type_page/index.html',
                {'form': form}
            )

class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = "type_page/user_form.html"
    success_url = 'typer/'


class UserLogoutView(View):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('index')
        else:
            return redirect('login')