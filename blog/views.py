from django.shortcuts import render
from django.utils import timezone
from .models import Post

def employee_search(request):
       employee_name = request.POST.get('emp_name', '')

if employee_name == '':
       return render(request, 'blog/search/', {'employees': ''})
else:
       employees == Employee.objects.filter(name=employee_name)
       return render(request, 'blog/search/', {'employees': employees})
