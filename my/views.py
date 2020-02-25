from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *


def index(request):
    hoods = Neighborhood.objects.all()
    return render(request, 'main/index.html', {'hoods':hoods})

@login_required(login_url='/accounts/login/?next=/')
def hood(request,id):
    hoods = Neighborhood.objects.get(id=id)
    bus = hoods.business_set.all
    posts  = hoods.post_set.all
    return render(request, 'main/hood.html', {'hoods':hoods, 'bus':bus, 'posts':posts})

def profile(request):
      current_user = request.user
      profile = Profile.objects.filter(user=current_user).first()
      posts = request.user.post_set.all()

      return render(request, 'main/profile.html', {"posts": posts, "profile": profile, 'current_user':current_user})


def update_profile(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        form =  ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
        return render(request,'main/update_profile.html', {'form':form})


def add_post(request,id):
        current_user = request.user
        hoods = Neighborhood.objects.get(id=id)
        if request.method == 'POST':
                form = PostForm(request.POST, request.FILES)
                if form.is_valid():
                        addpost=form.save(commit=False)
                        post.hood = hoods
                        addpost.user = current_user
                        addpost.save()
                return redirect('hood',hoods.id)
        else:
            form = PostForm()
            return render(request,'main/new_post.html', {"form":form, 'hood':hoods})        
