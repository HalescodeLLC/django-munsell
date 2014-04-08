from django.shortcuts import render
from django.http import HttpResponse

from .models import MunsellColor


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        color = MunsellColor.objects.get(munsell_name=request.POST['munsell_color'])
        rgb = color.convert_to_standard_rgb()
        rgb_val = '%s %s %s' % (rgb[0], rgb[1], rgb[2])
        return HttpResponse(request, 'mcolor/home.html', {'rgb_val': rgb_val})
    return render(request, 'mcolor/home.html')
