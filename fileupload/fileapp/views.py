from django.shortcuts import render
from .forms import UploadFileForm
from .models import ImageModel

def fileupload(request):
    data = dict()
    if "GET" == request.method:
        return render(request, 'file.html', data)

    files = request.FILES
    image = files.get("image")
    instance = ImageModel()
    instance.image = image
    instance.save()
    return render(request, 'file.html', data)

