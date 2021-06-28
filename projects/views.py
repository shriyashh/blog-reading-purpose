from django.shortcuts import render
from .models import Project



def projectdetail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/projectdetails.html', context)







