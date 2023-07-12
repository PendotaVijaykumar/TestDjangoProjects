from django.shortcuts import render
from .forms import FeedbackForm

# Create your views here.
def FeedbackForm_view(request):
    form=FeedbackForm()
    sent=False
    if request.method=='POST':

        form=FeedbackForm(request.POST)
        if form.is_valid():
            print("Basic validation is succesfull")
            print("Name is :", form.cleaned_data['name'])
            print("Roll num is :",form.cleaned_data['roolnum'])
            print("Feedback is :", form.cleaned_data['feedback'])
            sent=True
            #return render(request,'testapp/thankyou.html',{'sent':sent})
    return render(request, 'testapp/home.html',{'form':form,'sent':sent})
def thankyou(request):
    return render(request,'testapp/thankyou.html')
