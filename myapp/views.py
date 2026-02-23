from django.shortcuts import render, redirect

from django.views.generic import View
# Create your views here.
from myapp.models import Todo

from .forms import TodoForm, RegistrationForm, SignInForm

from django.contrib.auth import authenticate, login, logout

from django.shortcuts import get_object_or_404, redirect

from myapp.decortors import signin_required

from django.utils.decorators import method_decorator


# signup, signin, signout

class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance = RegistrationForm()

        return render(request,"signup.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance = RegistrationForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()           

            return redirect("sign-in")

        else:        

            return render(request,"signup.html",{"form":form_instance})
        

class SignInView(View):

    def get(self,request,*args,**kwargs):

        form_instance = SignInForm()

        return render(request,"sign_in.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance = SignInForm(request.POST)

        if form_instance.is_valid():

            user_obj = authenticate(request,**form_instance.cleaned_data)

            if user_obj:

                login(request,user_obj)

                return redirect("todos")          

            
        return render(request,"sign_in.html",{"form":form_instance})







@method_decorator(signin_required,name="dispatch")
class TodoCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance = TodoForm()


        # listing

        qs = Todo.objects.filter(owner=request.user)
       

        return render(request,"todo_create.html",{"form":form_instance,"todos":qs})
    

    def post(self,request,*args,**kwargs):

        form_instance = TodoForm(request.POST)

        if form_instance.is_valid():

            form_instance.instance.owner = request.user

            form_instance.save()

            return redirect("todos")

        return render(request,"todo_create.html",{"form":form_instance})


def todo_toggle_status(request, pk):
    todo = get_object_or_404(Todo, id=pk, owner=request.user)
    todo.status = not todo.status
    todo.save()   
 
    return redirect("todos")

@method_decorator(signin_required,name="dispatch")
class TodoEditDeleteView(View):

    def get(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        Todo.objects.get(id=id).delete()

        return redirect("todos")


class SignOutView(View):
    def post(self, request):
        logout(request)
        return redirect('sign-in')