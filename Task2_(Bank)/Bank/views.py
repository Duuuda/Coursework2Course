from django.shortcuts import render
from Bank.handler import handler

# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'Bank/index.html')
    elif request.method == 'POST':
        if request.path.strip('/') == 'calculate':
            input_text = request.POST.get('input')
            return render(request, 'Bank/index.html', context={'input': input_text, 'output': handler(input_text)})
        elif request.path.strip('/') == 'clear':
            return render(request, 'Bank/index.html')
    return render(request, 'Bank/index.html')
