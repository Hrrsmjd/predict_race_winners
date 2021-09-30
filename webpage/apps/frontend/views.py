from django.shortcuts import render


def Index(request):
    return render(request, './index.html')

def HowTo(request):
    return render(request, './howto.html')

def Predict(request):
    return render(request, './predict.html')