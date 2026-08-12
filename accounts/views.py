from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import SignupForm
from .models import Profile



def signup(request):

    if request.method == "POST":

        form = SignupForm(request.POST)

        if form.is_valid():

            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )


            Profile.objects.create(
                user=user,
                full_name=form.cleaned_data["full_name"],
                phone=form.cleaned_data["phone"]
            )


            login(request,user)

            return redirect("home")


    else:
        form = SignupForm()


    return render(
        request,
        "registration/signup.html",
        {"form":form}
    )