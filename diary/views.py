
from django.shortcuts import render,redirect
from .models import *
from .forms import EntryForm


def index(request):
    entries = Diary.objects.filter(user=request.user)
    context = {'entries' : entries}
    return render(request, 'diary/index.html',context)

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.user = request.user
            new_entry.save()
            return redirect('diary_home')
    else:
        form = EntryForm()
    
    return render(request, 'diary/add.html', {'form': form})
