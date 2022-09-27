from django.shortcuts import render, redirect
from .models import Dog
from django.urls import reverse
# Create your views here.


def list(request):
    list_of_dogs = Dog.objects.all()
    print(list_of_dogs)
    my_list = {'all_dogs': list_of_dogs}
    #print(context)
    my_var ={"name":"Katinka"}
    return render(request, 'dogs/list.html',  context=my_list)


def add(request):
    if request.POST:
        name = request.POST["name"]
        age = request.POST["age"]
        color = request.POST["color"]
        breed = request.POST["breed"]
        isBiting = request.POST.get("isBiting", False)
        sex = request.POST["sex"]
        isBiting = True if isBiting == "on" else False
        tmpDog = Dog(name=name, age=age, color=color, breed=breed, isBiting=isBiting, sex=sex)
        print(tmpDog)
        print(name, age, color, breed, isBiting, sex)
        Dog.objects.create(name=name, age=age, color=color, breed=breed, isBiting=isBiting, sex=sex)
        return redirect(reverse('dogs:list'))
    else:
        return render(request, 'dogs/add.html')


def delete(request):
    if request.POST:
        print(request.POST["dog"])
        pK = int(request.POST["dog"])
        print(type(request.POST["dog"]))
        Dog.objects.get(pk=pK).delete()
        return redirect(reverse('dogs:list'))
    else:
        list_of_dogs = Dog.objects.all()
        print(list_of_dogs)
        my_list = {'all_dogs': list_of_dogs}
        return render(request, 'dogs/delete.html', context=my_list)