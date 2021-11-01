from django.shortcuts import render
from django.http import HttpResponse

def university(request):

    # ja submit, tad metode POST
    if request.method == 'POST':

        full_name = request.POST['full_name']
        math = request.POST['math']
        lat = request.POST['lat']
        eng = request.POST['eng']
    # if int(math) >39:
        total = int(math) + int(lat) + int(eng)

        if int(math) > 39 and int(lat) > 39 and int(eng) > 39:
            return HttpResponse(f'Dear {full_name} velcome to university! Your total score is: {total}')
        else:
            return HttpResponse(f'Dear loser {full_name} university is not for you, see u later, may be...')

    return render(
        request,
        template_name='action.html',
    )