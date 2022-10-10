from django.shortcuts import redirect, render
from .forms import FeedbackForms
# Create your views here.



def Feedbackindex(request):
    data = FeedbackForms(request.POST)
    if request.method == "POST":
        if data.is_valid():
            data.save()
            return redirect('Feedbackindex')
        else:
            return render(request,"feedback.html",{'data':data})
    return render(request,"feedback.html",{'data':data})