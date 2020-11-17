from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


from .forms import RegisterForm
from .models import Tagihan, Uses


def index(request):
    return render(request, 'home/index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:home')
    else:
        form = RegisterForm()
    return render(request, 'registration/login.html', {'page': 'register', 'form': form})


@login_required
def myBill(request):
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
    data = Tagihan.objects.filter(custommer=request.user, status=False)
    page = Paginator(data, 50)
    PageNum = request.GET.get('page')
    data_result = page.get_page(PageNum)
    return render(request, 'home/my-bill.html', {'data': data_result})


def dont_have_acces(request):
    return render(request, 'home/dont-have-access.html')


def notFound(request):
    return render(request, 'home/404.html')