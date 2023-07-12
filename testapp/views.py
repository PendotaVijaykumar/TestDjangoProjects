from django.shortcuts import render
from testapp.forms import MovieForm
from testapp.models import Movie

# Create your views here.
def index_view(request):
    return render(request, 'testapp/index.html')

def add_movie(request):
    form=MovieForm()
    if request.method=='POST':
        form1=MovieForm(request.POST)
        if form1.is_valid():
            name=form1.cleaned_data['MovieName']
            movies_list=Movie.objects.all().order_by('MovieName')
            print("name is :",name)
            #print("movies_list is:",movies_list)
            for movie in movies_list:
                if movie.MovieName==name:
                    print("movie is already existed in database..")
                    return render(request, 'testapp/index2.html',{'form':form1S})
                    break



            form1.save()
        return index_view(request)
    return render(request, 'testapp/addmovie.html',{'form':form})

def list_view(request):
    movies_list=Movie.objects.all().order_by('-ReleaseDate')
    return render(request, 'testapp/list.html',{'movies_list':movies_list})
def testview(request):
    pass
