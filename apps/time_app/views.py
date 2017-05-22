# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.utils.timezone import utc
import pytz
from pytz import timezone

def index(request):
    cal = timezone('US/Pacific')

    utc_time = utc.localize(datetime.now())  #time in utc

    #convert to PST
    local_day = utc_time.astimezone(cal).strftime('%b %d, %Y')
    local_time = utc_time.astimezone(cal).strftime('%I:%M %p')

    print local_day     #for debugging
    print local_time    #for debugging

    #pass date/time with context object
    context = {
        'day' : local_day, 
        'time' : local_time
    }
    return render(request, 'time_app/index.html', context)
