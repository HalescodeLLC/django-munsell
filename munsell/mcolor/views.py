from django.shortcuts import render
# from django.http import HttpResponse

from .models import MunsellColor


# Create your views here.
def home_page(request):
    return render(request, 'mcolor/home.html')

def results_page(request):
    if request.method == 'POST':
        if '_exact_match' in request.POST:
            colors = MunsellColor.objects.filter(munsell_name=request.POST['munsell_color'].upper())
            query_color = request.POST['munsell_color']
            return render(request, 'mcolor/results.html', {'colors': colors, 'query_color': query_color})
        else:
            query_color = request.POST['munsell_color']
            colors = MunsellColor.objects.filter(sortable_name__icontains=request.POST['munsell_color'].replace(' ',''))
        return render(request, 'mcolor/results.html', {'colors': colors, 'query_color': query_color})
    return render(request, 'mcolor/home.html')
