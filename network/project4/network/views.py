from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth import get_user_model

from .models import User,post


def index(request):

   return render(request, "network/index.html", {
           "post":post.objects.all(),
    })

def upload(request):
    print ("we are in upload")
    return HttpResponse ('upload fuction')

''''
class postForm(forms.Form):
      pid = forms.IntegerField()
      title = forms.CharField(label='title', max_length=100)
      comment = forms.CharField(label='comment',max_length=300 )
'''

class postForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('des_content',)

def addpost(request):
    if request.method != "POST":
        print (f'Not a post mentod')  
        return HttpResponse ('Not a post call')
    else: 
        form = postForm(request.POST)
        #title = form['title']
        #comment = form['comment']
        #print (f'Form :  {title.value()} ') 
        #print (f'Form :  {comment} ')  
        #return HttpResponse (form)

        if form.is_valid():
            title = form.cleaned_data['title']
            comment = form.cleaned_data['comment']
            p_record = post(author_id=request.user.id  ,title=title, des_content=comment, likes =0,status ='True' )
            p_record.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/index.html")
            #return HttpResponse ('Form not valid')
def updatepost(request):
    print(f'we are in updatepost')
    if request.method != "POST":
        print (f'Not a post mentod')  
        return HttpResponse ('Not a post call')
    else: 
        form = postForm(request.POST)
        if form.is_valid():
            print(f'we are in Post form validation')
            #comment is the id in index
            des_content= request.POST.get('postComment')
            print(f'des_content' , des_content)
            pid = request.POST.get('postId')
            print(f'pid: ')
            print(pid)
            t =post.objects.get(id=pid) 
            print ('post id :')
            print (pid)
            print ('des_content :')
            print (des_content)
            if (des_content):
              t.des_content = des_content
            else: 
              t.des_content = "des_contenttt"
            t.save()
            #return HttpResponseRedirect(reverse("index"))
            return HttpResponse(status=204)
        else:
            return render(request, "network/index.html")
            #return HttpResponse ('Form not valid')


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
