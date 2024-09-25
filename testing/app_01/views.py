import json
from django.shortcuts import render
from app_01.forms import UploadFilesForm
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
                addres_ip = d_new.get('remote_ip')
                data = d_new.get('time')
                method_url = d_new.get('request')
                method = method_url.split(' ')[0]
                url = method_url.split(' ')[1]
                answer = int(d_new.get('response'))
                answer_size = int(d_new.get('bytes'))
                print(f'{data=}\n{method=}\n{url=}\n{answer=}\n{answer_size=}\n\n')

            return render(request, 'app_01/index.html',{"form": form})
    else:
        form = UploadFilesForm()
        return render(request, 'app_01/index.html',{"form": form})