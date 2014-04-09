from django.shortcuts import render
from django.http import HttpResponse

from .models import MunsellColor


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        colors = MunsellColor.objects.filter(munsell_name__contains=request.POST['munsell_color'])
        rgb_vals = []
        for color in colors:
            rgb = color.convert_to_standard_rgb()
            rgb_vals.append(rgb[0] + ' ' + rgb[1] + ' ' + rgb[2])
        return render(request, 'mcolor/home.html', {'rgb_vals': rgb_vals})
    return render(request, 'mcolor/home.html')
