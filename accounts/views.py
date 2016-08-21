from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from accounts.forms import LoginForm
# Create your views here.

def index(request):
    loginform = LoginForm()
    context = {'form':loginform}
    return render(request,'index.html',context)

@require_POST
def login_view(request):
    filled_form = LoginForm(request.POST)
    if filled_form.is_valid():
        user = filled_form.get_user()
        context = { 'user': user }
        return render(request,'home.html',context)
