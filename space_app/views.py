from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse
from .models import Planet, Item


def index(request):
    request.session.clear()
    context = {
        "planets": Planet.objects.all()
    }
    return render(request, 'index.html', context)

def planet(request, id):
    # request.session.clear()
    context = {
        "planet_to_show": Planet.objects.get(id=id),
        "items": Item.objects.all()
    }
    planet = Planet.objects.get(id=id)
    request.session['planet_length'] = '{:,}'.format(int(planet.longest_dist))
    return render(request, 'planet_info.html', context)

def measure(request, item_id, planet_id):
    
    item = Item.objects.get(id=item_id)
    planet = Planet.objects.get(id=planet_id)
    planet_length_ft = planet.longest_dist*5280
    total = planet_length_ft/item.length
    planet_l = planet.longest_dist
    item_l = item.length
    request.session['amount'] = '{:,}'.format(int(total))
    request.session['the_item'] = item.item_name
    request.session['item_length'] = '{:,}'.format(item_l)
    request.session['sentence'] = ('Oh the %s! It will take %s of those to get to %s from the Earth!' % (request.session['the_item'], request.session['amount'], planet.name) )
    return redirect(f'/planet/{planet.id}')

def create(request):
    return render(request, 'create_planet.html')

def add(request):
    Planet.objects.create(name=request.POST['name'], desc=request.POST['desc'], longest_dist=request.POST['longest_dist'], shortest_dist=request.POST['shortest_dist'], image=request.POST['image'])
    return redirect('/')

def update(request, id):
    context = {
        "planet": Planet.objects.get(id=id)
    }
    return render(request, 'update.html', context)

def updatePlanet(request,id):
    planet_to_update = Planet.objects.get(id=id)
    planet_to_update.name = request.POST['name']
    planet_to_update.desc = request.POST['desc']
    planet_to_update.longest_dist = request.POST['longest_dist']
    planet_to_update.shortest_dist = request.POST['shortest_dist']
    planet_to_update.image = request.POST['image']
    planet_to_update.save()
    return redirect('/')


