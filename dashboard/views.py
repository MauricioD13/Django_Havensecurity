from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from dashboard.models import ID_table
# Create your views here.
import random

ids = {}
gas = {}
temp = []
temp_values = []
gas_values = []
for i in range(5):
    temp.append(random.randint(10, 35))

for i in range(5):
    aux = random.randint(300, 800)
    gas_values.append(aux)
    gas[str(aux)] = '0' + str(random.randint(1, 30)) + '/' + '0' + str(random.randint(1, 12))

for i in range(5):
    aux = random.randint(10000, 100000)
    ids[str(aux)] = i


@login_required
def dashboard(request):

    return render(request, 'dashboard/dashboard.html', {
        'gas': gas,
        'temp': temp,
    })


@login_required
def dashboard_rfid(request):
    return render(request, 'dashboard/dashboard_rfid.html', {
        'ids': ids,
    })
