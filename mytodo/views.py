from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


# Create your views here.


def index(request):
    # fetch and push my data
    records = Todo.objects.all()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    context = {
        "records": records,
        "form": form
    }
    return render(request, 'mytodo/index.html', context)


def delete_todo(request, pk):
    Todo.objects.filter(id=pk).delete()
    Todo.objects.all()
    return redirect('index')
