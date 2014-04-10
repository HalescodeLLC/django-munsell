from django.shortcuts import render
# from django.http import HttpResponse

from .models import MunsellColor


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        colors = MunsellColor.objects.filter(sortable_name__icontains=request.POST['munsell_color'].replace(' ',''))
        rgb_vals = []
        for color in colors:
            rgb = color.convert_to_standard_rgb_single_string()
            rgb_vals.append(rgb)
        return render(request, 'mcolor/home.html', {'rgb_vals': rgb_vals, 'colors': colors})
    return render(request, 'mcolor/home.html')
