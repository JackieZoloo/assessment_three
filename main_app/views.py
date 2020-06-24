from django.shortcuts import render, redirect
from .models import Wish
from django.views.generic.edit import CreateView

# Create your views here.

def home(request):
    return render(request, 'main_app/index.html', {
        'wishes': Wish.objects.all()
    })
class WishCreate(CreateView):
    model = Wish
    fields = '__all__'
    template_name = "main_app/create.html"
    
def wish_create(request):
    Wish.objects.create(wish_list=request.POST['wish_list'])
    return redirect('home')
def delete(request, id):
    Wish.objects.get(id=id).delete()
    return redirect('home')