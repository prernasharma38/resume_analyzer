from django.shortcuts import render
from .utils import extract_info
from django.core.files.storage import FileSystemStorage

def upload_resume(request):
    if request.method == 'POST' and request.FILES['resume']:
        resume = request.FILES['resume']
        fs = FileSystemStorage()
        filename = fs.save(resume.name, resume)
        filepath = fs.path(filename)
        data = extract_info(filepath)
        return render(request, 'upload.html', {'data': data})
    else:
        return render(request, 'upload.html')
