from django.shortcuts import render, redirect
from .models import Bug

def bug_list(request):
    bugs = Bug.objects.all()
    return render(request, 'tracker/bug_list.html', {'bugs': bugs})

def add_bug(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        status = 'Open'

        Bug.objects.create(title=title, description=description, priority=priority, status=status)
        return redirect('bug_list')
    return render(request, 'tracker/add_bug.html')
