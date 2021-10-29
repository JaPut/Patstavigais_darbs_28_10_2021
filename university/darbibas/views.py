from django.shortcuts import render
from django.http import HttpResponse

def university(request):

    # ja submit, tad metode POST
    if request.method == 'POST':

        full_name = request.POST['full_name']
        math = request.POST['math']
        lat = request.POST['lat']
        eng = request.POST['eng']
        total = int(math) + int(lat) + int(eng)

        if total > 39:
            return HttpResponse(f'Dear {full_name} velcome to the party! Your total score is: {total}')
        else:
            return HttpResponse(f'Dear loser {full_name} see u later, may be...')

    return render(
        request,
        template_name='action.html',
    )