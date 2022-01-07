from django.shortcuts import render
from django.contrib import messages
from .models import Car, Driver


def car_detail(request, pk):
    owner_obj = Driver.objects.get(pk=pk)

    car_objs = Car.objects.filter(owner_id=owner_obj.id)

    context = {

        "vehicles": car_objs,

        "drivers": owner_obj,

    }

    return render(request, "car_detail.html", context)


def showdata(request):
    results = Driver.objects.all()
    return render(request, 'base.html', {"data": results})


def insertemp(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('license'):
            saverecord = Driver()
            saverecord.name = request.POST.get('name')
            saverecord.license = request.POST.get('license')
            saverecord.save()
            messages.success(request,'driver  '+saverecord.name+' is saved')
            return render(request,'insert.html',{})
    else:
        return render(request,'insert.html',{})
