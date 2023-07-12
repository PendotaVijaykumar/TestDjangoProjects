from django.shortcuts import render

# Create your views here.
def Home(request):

    #first=request.GET['first']
    #second=request.GEt['Second']

    return render(request, 'testapp/home.html')

def lcm(request):
    n1=int(request.GET['first'])
    n2=int(request.GET['second'])

    #sum=int(n1)+int(n2)
    #print(n1,n2)
    max=0
    lcm=0
    if int(n1)>int(n2):
        max=int(n1)
    else:
        max=int(n2)
    while(True):
        if(max%n1 ==0 and max%n2==0):
            lcm=int(max)
            break
        else:
            max=int(max+1)

    return render(request, 'testapp/results.html' ,{'lcm':lcm})
