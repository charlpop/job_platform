from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from .models import Jobs




def jobs(request):
    return HttpResponse("Hello world!")

def login(request):
    success_message = None
    error_message = None
    if request.method == "POST":
          print(request.POST)
        #   creating s django user
        # retriving the details sent in
    email = request.POST['email']
    password = request.post['password']
    # creating a user
    # user = User(username=email, password=password)
    try :
         user = User.objects.create_user(username=email, password=password)
         success_message = 'login successful'
    except Exception as e :
     print(e)
    print('error occured login user')







    return render(request, "login.html", {})


