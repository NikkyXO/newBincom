from django.shortcuts import render
from django.contrib import messages
from base.models import AnnouncedPuResults, PollingUnit, Lga, Party, AnnouncedLgaResults
# Create your views here.


def index(request):
    parties = Party.objects.all()
    if request.POST:
        data = request.POST
        unit = PollingUnit.objects.create(polling_unit_name=data['unit_name'])
        scores = data['party_score']
        index = 0
        for a in parties:
            pu_result = AnnouncedPuResults.objects.create(
                party_score = scores[index], party_abbreviation= a.partyname,
                polling_unit_uniqueid = unit.uniqueid
            )
            index +=1
        messages.success(request, 'Polling Unit Result Added Successfully')    
    context = {
        'parties' : parties
    }
    return render(request, 'index.html', context)

def polling_units(request):
    units = PollingUnit.objects.all()
    context = {
        'units' : units
    }
    return render(request, 'units.html', context)

def pu_result(request, id):
    unit = PollingUnit.objects.get(uniqueid=id)
    results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=unit.uniqueid) 
    context = {
        'unit':unit,
        'results':results
    }
    return render(request, 'pu-result.html', context)

def lgas(request):
    lgas = Lga.objects.all()
    context = {
        'lgas' : lgas
    }
    return render(request, 'lgas.html', context)

def lga_result(request, id):
    lga = Lga.objects.get(lga_id=id)
    lga_r = AnnouncedLgaResults.objects.filter(lga_name=lga.lga_id)
    units = PollingUnit.objects.filter(lga_id=id).values_list('polling_unit_id', flat=True)
    parties = [{'party': a.partyname, 'score' : 0} for a in Party.objects.all()]
    unit_lga_result = AnnouncedPuResults.objects.filter(polling_unit_uniqueid__in=units) 
    for p in parties:
        scores = sum([a.party_score for a in unit_lga_result.filter(party_abbreviation=p['party'])])
        p['score'] = scores

    context = {
        'parties' : parties,
        'lga' : lga,
        'lga_r' : lga_r
    }
    return render(request, 'lga-result.html', context)

def all_party_newPU(request, id):
    new_unit = PollingUnit.objects.get(uniqueid=id)
    parties = Party.objects.all()




    context = {
        'lgas' : lgas
    }
    return render(request, 'lgas.html', context)