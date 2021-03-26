from django.shortcuts import render
from django.shortcuts import reverse
from  django.http import HttpResponse
from blogging.models import Details
from blogging.models import Login 
from blogging.models import Data
from blogging.forms import LoginForm 
from django.views.generic import (TemplateView, RedirectView, CreateView, ListView, DeleteView, DetailView)
# Create your views here.

#def login(request):
    # content = Login.objects.all()
    # print(content)
    # L=Login()
    #Log = LoginForm(request.POST)
    #if Log.is_valid():
       # u_name=Log.cleaned_data["username"]
        #u_pwd=Log.cleaned_data["password"]
        #Det = Login(u_name=u_name,u_pwd=u_pwd)
        #Det.save()
    # if request.method=="POST":
        # L.u_name=request.POST.get('fname')
        # L.u_pwd=request.POST.get('lname')
        # L.save()
    #return render(request,"login.html",{"context":Log})


class Home(TemplateView):
    template_name="home.html"



# def details(request):
    # content = Details.objects.all()
    # content = Data.objects.all()
    # print(content)
    # D=Details()

    # if request.method=="POST":
        # D.u_name=request.POST.get('fname')
        # D.u_pwd=request.POST.get('lname')
        # D.u_email=request.POST.get('email')
        # D.u_number=request.POST.get('number')
        # D.save()

    # return render(request,"details.html")



class Data_to_get_post(CreateView):
    template_name="post.html"
    model = Data
    fields = "__all__"
    def get_success_url(self):
        return reverse("home")


class Login_page(CreateView):
    template_name = "login.html"
    model = Login
    fields = "__all__"
    def get_success_url(self):
        return reverse("data")


class Details_page(CreateView):
    template_name = "details.html"
    model = Details
    fields = "__all__"
    def get_success_url(self):
        return reverse("login")


class Show_all_blogs(ListView):
    template_name = "home.html"
    # model = Data
    queryset = Data.objects.all()
    # def get_queryset(self,*args,**kwargs):
    #     q=super(Show_all_blogs,self).get_queryset(*args,**kwargs)
    #     print(q)
    #     print(Data.objects.all())
    #     return q

class Show_details(DetailView):
    template_name="details.html"
    model = Data


class Delete_Blog(DeleteView):
    template_name="delete.html"
    model=Data
    def get_success_url(self):
        return reverse("home")





# def data(request):
    # content = Data.objects.all()
    # print(content)
    # print(request.GET)
    # Dat = Data()
    # if request.method=="POST":
        # Dat.u_name=request.POST.get('textarea')
    # return render(request,"data.html")


