from django.shortcuts import render, redirect
from .forms import ParentForm
from .models import Parent

def parent_list(request):
    parents = Parent.objects.all()
    return render(request, 'parents/parent_list.html', {
        'parents': parents
    })

def add_parent(request):
    if request.method == "POST":
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_parent')
    else:
        form = ParentForm()

    return render(request, 'parents/add_parent.html', {'form': form})