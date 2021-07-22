from frontend.models import Shipment
from django.shortcuts import render
from .filters import ShipmentFilter

# Create your views here.
def home(request):

    return render(request, 'frontend/index.html')

def track(request):
    if request.method == 'POST':
        search = request.POST['search']
        products = Shipment.objects.filter(ship_code__contains=search)
        return render(request, 'frontend/track.html', {'search':search, 'products':products})
    else:
    # shipment = ship._set
    # myFilter = ShipmentFilter(request.GET, queryset=ship)
    
        return render(request, 'frontend/track.html')
        # return render(request, 'frontend/track.html', {'filter':myFilter, 'result':ship})


def search_order(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        orders = Shipment.objects.filter(ship_code__contains=searched)
        return render(request, 'frontend/search_order.html', {'searched':searched, 'orders':orders})
    else:
        return render(request, 'frontend/search_order.html')
