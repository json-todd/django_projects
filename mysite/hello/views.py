from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_view(request):
    visit_count = request.session.get('visit_count', 0) + 1
    request.session['visit_count'] = visit_count

    response =  HttpResponse(f'view count={str(visit_count)}')
    response.set_cookie('dj4e_cookie', '223c4a00', max_age=1000)

    return response
