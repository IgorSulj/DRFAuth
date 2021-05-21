from django.shortcuts import render
from .forms import UserForm

# Create your views here.


def form_view(request):
    form = UserForm()
    context = {'form': form}
    return render(request, 'form.html', context)
