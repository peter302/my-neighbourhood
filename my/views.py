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
