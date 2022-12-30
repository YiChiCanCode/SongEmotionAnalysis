from django.shortcuts import render
from .forms import AudioForm
from django.http import HttpResponse

#view before uploading
def home(request):
    if request.method=='POST':
        form = AudioForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = AudioForm
    
    return render(request, 'index.html', {'form':form})


def getPredictions(id):
    #fetch user's uploaded song based on user's id
    #pickle to predict the model, should come back later
    path = ''
    return path


#view after uploading
def result(request):
    #should use getPredictions() and settle the result
    #render result page with result

    #return render(request, 'result.html', {'result':result})
    return render(request, 'result.html')
