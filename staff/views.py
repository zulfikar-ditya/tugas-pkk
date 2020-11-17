from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


from my_app.views import dont_have_acces, notFound
from my_app.models import User, Uses, Months, Tagihan, PayMent, Tarif

from .forms import UsesForm

import datetime

'''
@login_required
def (request):
    if request.user.is_staff or request.user.is_superuser:
        return render(request, 'staff/.html')
    else:
        return dont_have_acces(request)
'''


@login_required
def index(request):
    if request.user.is_staff or request.user.is_superuser:
        return render(request, 'staff/index.html')
    else:
        return dont_have_acces(request)


# Uses Model
@login_required
def add_uses_id(request):
    if request.user.is_staff or request.user.is_superuser:
        if request.method == 'POST':
            try:
                user = User.objects.get(username=request.POST['user'])
                return HttpResponseRedirect(f'../add/{user}/')
            except (KeyError, User.DoesNotExist):
                messages.error(request, 'custommer not found')
            
        return render(request, 'staff/power-used/add-uses-id.html')
    else:
        return dont_have_acces(request)


@login_required
def addUses(request, username):
    if request.user.is_staff or request.user.is_superuser:
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'custemmer not found')
            return redirect('staff:add_uses_id')
        if request.method == 'POST':
            form = UsesForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.custommer = user
                instance.save()
                messages.success(request, 'Data Saved')
                return redirect('staff:powerUsedList')
        else:
            form = UsesForm()
        return render(request, 'staff/power-used/add-uses.html', {
            'user': user,
            'form': form,
        })
    else:
        return dont_have_acces(request)


@login_required
def powerUsedList(request):
    if request.user.is_staff or request.user.is_superuser:
        data = Uses.objects.all()
        return render(request, 'staff/power-used/list.html', {
            'data': data,
        })
    else:
        return dont_have_acces(request)


@login_required
def editPowerUsed(request, id):
    if request.user.is_staff or request.user.is_superuser:
        month = Months.objects.all()
        try:
            data = Uses.objects.get(pk=id)
        except:
            return notFound(request)
        user = User.objects.get(username=data.custommer)
        if request.method == "POST":
            data.month = Months.objects.get(pk=request.POST['month'])
            data.year = request.POST['year']
            data.meter_start = request.POST['meter_start']
            data.meter_end = request.POST['meter_end']
            data.save()
            messages.success(request, 'Data Updated')
            return redirect('staff:powerUsedList')

        return render(request, 'staff/power-used/edit.html', {
            'data': data,
            'month': month,
        })
    else:
        return dont_have_acces(request)


# Bill Pages
@login_required
def autoAddBill(request):
    if request.user.is_staff or request.user.is_superuser:
        uses = Uses.objects.all()
        tagihan = Tagihan.objects.all()
        for i in uses:
            try:
                tagihan_item = Tagihan.objects.get(uses=i.id)
            except:
                new = Tagihan()
                new.custommer = i.custommer
                new.uses = i
                new.month = i.month
                new.year = i.year
                new.sum_meter = int(i.meter_end) - int(i.meter_start)
                new.save()
        tagihan = Tagihan.objects.filter(status=False)
        return render(request, 'staff/bill/list.html', {'tagihan': tagihan})
    else:
        return dont_have_acces(request)


# payment pages
def paymentConfirm(request, id):
    if request.user.is_staff or request.user.is_superuser:
        try: 
            tagihan = Tagihan.objects.get(pk=id, status=False)
        except:
            return notFound(request)
        custommer = User.objects.get(username=tagihan.custommer)
        tarif = Tarif.objects.get(pk=custommer.id)
        new = PayMent()
        new.tagihan = tagihan
        new.custommer = custommer
        new.month = tagihan.month
        new.biaya_admin = 5000
        new.sumPayment = (int(tagihan.sum_meter) * int(tarif.tarif)) + new.biaya_admin
        if request.method == "POST":
            tagihan.status = True
            tagihan.save()
            new.save()
            return redirect('staff:paymentlist')
        return render(request, 'staff/payment/confirm.html', {
            'tagihan': tagihan,
            'new': new,
            'tarif': tarif
        })
    else:
        return dont_have_acces(request)


@login_required
def paymentlist(request):
    if request.user.is_staff or request.user.is_superuser:
        data = PayMent.objects.all()
        return render(request, 'staff/payment/list.html', {'data': data})
    else:
        return dont_have_acces(request)
        
