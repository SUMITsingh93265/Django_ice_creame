from django.shortcuts import render, redirect
from datetime import datetime
from home.models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Sum
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def chocolate(request):
    return render(request, "chocolate.html")


def dry_fruit(request):
    return render(request, "dry_fruit.html")


def choco_chip(request):
    return render(request, "choco_chip.html")


def family_icecream(request):
    return render(request, "family_icecream.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(
            request, "Your franchie form submit successfully!! Thank you")

        return redirect('/contact/')

    return render(request, "contact.html")


def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        feedback = Feedback(name=name, email=email, phone=phone, desc=desc)
        feedback.save()
        messages.success(
            request, "Your feedback form submit successfully!! Thanks for your feedback")

        return redirect('/contact/')

    return render(request, "contact.html")


@login_required(login_url='/login')
def ice_recipes(request):
    if request.method == "POST":
        data = request.POST
        ice_image = request.FILES.get('ice_image')
        ice_name = data.get('ice_name')
        ice_discription = data.get('ice_discription')

        Ice_recipe.objects.create(
            ice_image=ice_image,
            ice_name=ice_name,
            ice_discription=ice_discription,
        )
        return redirect('/ice_recipes')

    queryset = Ice_recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(
            ice_name__icontains=request.GET.get('search'))

    context = {'ice_recipes': queryset}

    return render(request, "ice_recipes.html", context)


def update_recipe(request, id):
    queryset = Ice_recipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        ice_image = request.FILES.get('ice_image')
        ice_name = data.get('ice_name')
        ice_discription = data.get('ice_discription')

        queryset.ice_name = ice_name
        queryset.ice_discription = ice_discription

        queryset.save()
        return redirect('/ice_recipes')

    if request.GET.get('search'):
        queryset = queryset.filter

    context = {'recipe': queryset}

    return render(request, 'update_ice.html', context)


def delete_ice(request, id):
    queryset = Ice_recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/ice_recipes')


def login_pg(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username doesn't found.")
            return redirect('/login')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid password.")
            return redirect('/login')

        else:
            login(request, user)
            return redirect('/ice_recipes')

    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.warning(request, "Username already taken.")
            return redirect('register')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully.")
        return redirect('register')

    return render(request, "register.html")


def get_student(request):
    queryset = Student.objects.all()

    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks'))

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search)|
            Q(department__department__icontains = search)|
            Q(student_id__student_id__icontains = search)
            )

    paginator = Paginator(queryset, 25)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "report/student.html", {'queryset' : page_obj})

def see_marks(request, student_id):
    queryset = Subject_marks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))

    return render(request, "report/stu_marks.html", {'queryset' : queryset, 'total_marks' : total_marks})