from django.shortcuts import render, redirect, get_object_or_404
from home.models import PersonalDetail

# Create your views here.


def dashboard_view(request):
    details = PersonalDetail.objects.all()
    return render(request, "dashboard/dashbaord_views.html", {"details": details})



def dashboard(request):
    values = {'website_name': 'Django', 'website_age': 10, 'developer_name': 'Ganesh Doodam'}
    return render(request, 'dashboard/dashboard.html', values)


def edit(request, person_id):
    person = get_object_or_404(PersonalDetail, id=person_id)
    if request.method == 'POST':
        person.name = request.POST.get('name')
        person.email = request.POST.get('email')
        person.age = request.POST.get('age')
        person.save()
        return redirect('dashboard:dashboard_view')

    return render(request, 'dashboard/edit.html', {'person': person})


def delete(request, person_id):
    person = get_object_or_404(PersonalDetail, id=person_id)
    person.delete()
    return redirect('dashboard:dashboard_view')