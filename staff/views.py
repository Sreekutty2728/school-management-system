from django.shortcuts import render, redirect
from .forms import StaffForm
from .models import Staff

def add_staff(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_staff')
    else:
        form = StaffForm()

    return render(request, 'staff/add_staff.html', {'form': form})


def staff_list(request):
    staffs = Staff.objects.all()
    return render(request, 'staff/staff_list.html', {
        'staffs': staffs
    })