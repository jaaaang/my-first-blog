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

def upload(req):
    if req.method == 'POST':
        if 'file' in req.FILES:
            file = req.FILES['file']
            filename = file._name

            fp = open('%s/%s' % (C:\Users\sktelecom\Downloads, filename) , 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()
            return HttpResponse('File Uploaded')
    return HttpResponse('Failed to Upload File')
