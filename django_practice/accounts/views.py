from django.shortcuts import render
from django.shortcuts import redirect
from accounts.models import Account


def signin(request):
    return render(request, "signin.html")


def login_form(request):
    return render(request, "login_form.html")


def signin_insert(request):
    signin_id = request.POST["signin_id"]
    signin_pw = request.POST["signin_pw"]
    signin_pw2 = request.POST["signin_pw2"]

    if signin_pw != signin_pw2:
        return render(request, "signin.html", {"message_pw": "INCORRECT PASSWORD"})
    if Account.objects.filter(signin_id=signin_id).exists():
        return render(request, "signin.html", {"message_id": "EXISTING ID"}, status=401)

    Account.objects.create(signin_id=signin_id, signin_pw=signin_pw)
    return redirect('/')


def login(request):
    signin_id = request.POST["signin_id"]
    signin_pw = request.POST["signin_pw"]
    complete = "log_complete"

    if Account.objects.filter(signin_id=signin_id, signin_pw=signin_pw).exists():
        response = render(request, "home.html", {"log_complete": complete})
        response.set_cookie('signin_id', signin_id)
        response.set_cookie('signin_pw', signin_pw)
        return response
    else:
        return redirect("login_from.html")


def logout(request):
    response = redirect('/')
    response.delete_cookie('signin_id')
    response.delete_cookie('signin_pw')
    return response
