from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from dashboard.models import ID_table
# Create your views here.
import random

# Thingspeak

import urllib3
import json

#Dropbox

import dropbox

dbx = dropbox.Dropbox('KxL2v9KtxYwAAAAAAAAAAblg3U4IVJ9YS8iNJI2yowo9o6jv9l-6hVggIyRS49eq')
http = urllib3.PoolManager()

results = 10


@login_required
def dashboard(request):
    temp_values = []
    gas_values = []
    timestamp_values = []
    timestamp_str = http.request('GET', 'https://api.thingspeak.com/channels/1509577/fields/3.json?results=10')
    temp_str = http.request('GET','https://api.thingspeak.com/channels/1509577/fields/1.json?results=10')
    gas_str = http.request('GET','https://api.thingspeak.com/channels/1509577/fields/2.json?results=10')
    timestamp = json.loads(timestamp_str.data)
    temp = json.loads(temp_str.data)
    gas = json.loads(gas_str.data)
    
    for i in range(results):
        
        temp_values.append(temp['feeds'][i]['field1'])
        gas_values.append(gas['feeds'][i]['field2'])
        
        aux = timestamp['feeds'][i]['field3']
        if(aux == None):
            timestamp_values.append('0')
        else:
            timestamp_values.append(aux[:4]+'-'+aux[4:6]+'-'+aux[6:8]+' | '+aux[9:11]+':'+aux[11:13]+':'+aux[13:15])
        
    return render(request, 'dashboard/dashboard.html', {
        'results': results,
        'time': timestamp_values,
        'gas': gas_values,
        'temp': temp_values,
    })


@login_required
def dashboard_rfid(request):
    path_dbx = '/home/pi/HavenSecurity_IoT/codes'
    photo_id = 'https://www.dropbox.com/s/xmn3neyx9xkqit7/imagen_151_1.jpg?dl=0'
    ids = {}

    list_folder = dbx.files_list_folder(path_dbx)
    files = [list_folder.entries[idx].name for idx, value in enumerate(list_folder.entries)]
    for f in files:
        ids[f.split('_')[1]] = (dbx.files_get_temporary_link(path_dbx+'/'+f)).link
    
    if request.method == 'POST':
        new_ids = request.POST['photo_id_change']
        print(new_ids)
    return render(request, 'dashboard/dashboard_rfid.html', {
        'photo_id': photo_id,
        'ids': ids,
    })
