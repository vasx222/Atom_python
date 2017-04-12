from django.shortcuts import render
import datetime
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import render_to_response

def homepage(request):
    return HttpResponse("(.)(.)")

def hello(request):
    return HttpResponse("Hello, world!")

def showtime(request):
    current_date = datetime.datetime.now()
    # t = get_template('curtime')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    return render_to_response('curtime', locals())

def nexttime(request, offset):
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "Через %s часов будет %s" % (offset, dt)
    return HttpResponse(html)