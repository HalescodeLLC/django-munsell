from django.shortcuts import render
# from django.http import HttpResponse

from .models import MunsellColor


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        if '_exact_match' in request.POST:
            colors = MunsellColor.objects.filter(munsell_name=request.POST['munsell_color'].upper())
            return render(request, 'mcolor/home.html', {'colors': colors})
        else:
            colors = MunsellColor.objects.filter(sortable_name__icontains=request.POST['munsell_color'].replace(' ',''))
        return render(request, 'mcolor/home.html', {'colors': colors})
    return render(request, 'mcolor/home.html')
