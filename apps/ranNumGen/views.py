from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect

def index(request):
  try:
    request.session['times']
  except KeyError:
    request.session['times'] = 0

  return render(request, "ranNumGen/ranNum.html")

def ran_gen(request):
  request.session['times'] += 1
  request.session['ranword'] = get_random_string(length = 14)
  return redirect('/')

def reset(request):
  del request.session['times']
  del request.session['ranword']
  return redirect('/')
