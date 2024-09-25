import json
from django.shortcuts import render
from app_01.forms import UploadFilesForm
from app_01.models import Logg
# Create your views here.

def upload_file(request):
    if request.method == "POST":
        form = UploadFilesForm(request.POST,request.FILES)

        if form.is_valid():
            file = form.cleaned_data.get('file')
            obj = form.save(commit=False)
            obj.file = file
            obj.save()
            f = obj.file.open('r')
            dict = f.read()
            for d in dict.split('\n'):
                d_new = json.loads(d)
                address_ip = d_new.get('remote_ip')
                date = d_new.get('time')[:-15]
                time = d_new.get('time').split(date)[1][1:-6]
                method_url = d_new.get('request')
                method = method_url.split(' ')[0]
                url = method_url.split(' ')[1]
                answer = int(d_new.get('response'))
                answer_size = int(d_new.get('bytes'))
                Logg.objects.create(
                    date=date,
                    time = time,
                    address_ip= address_ip,
                    method = method,
                    url = url,
                    answer = answer,
                    answer_size = answer_size
                )
                context = {
                    "form" : form,
                    "title" : 'Загрузите файл',
                }
            return render(request, 'app_01/index.html',{"form": form})
    else:
        form = UploadFilesForm()
        return render(request, 'app_01/index.html',{"form": form})
    
def list_logs(request):
    context ={
        "title" : 'Результаты логгирования',
        "loggs" : Logg.objects.all(),
    }
    return render(request, 'app_01/logs.html', context = context)