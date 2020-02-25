from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *


def index(request):
    hoods = Neighborhood.objects.all()
    return render(request, 'main/index.html', {'hoods':hoods})
