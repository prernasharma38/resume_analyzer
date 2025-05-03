from django.shortcuts import render
from .utils import extract_info, store_resume_in_db, get_resumes_from_db
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

def upload_resume(request):
    if request.method == 'POST' and request.FILES['resume']:
        resume = request.FILES['resume']
        fs = FileSystemStorage()
        filename = fs.save(resume.name, resume)
        filepath = fs.path(filename)
        data = extract_info(filepath)
        store_resume_in_db(data)
        return render(request, 'upload.html', {'data': data})
    else:
        return render(request, 'upload.html')
    
def dashboard(request):
    if request.method == 'GET':
        filters = {
            'name': request.GET.get('name'),
            'email': request.GET.get('email'),
            'education': request.GET.get('education'),
            'hobbies': request.GET.get('hobbies'),
            'lifestyle': request.GET.get('lifestyle'),
        }
        # Remove None or empty string values from filters
        filters = {key: value for key, value in filters.items() if value}
        return render(request, 'dashboard.html', {'resumes': get_resumes_from_db(filters)})
    else:
        return HttpResponse('Invalid request method', status=400)
