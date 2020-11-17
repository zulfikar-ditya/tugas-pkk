from django.contrib import admin

from .models import Tarif, User, Months, Uses, Tagihan, PayMent


@admin.register(Tarif)
class TarifAdmin(admin.ModelAdmin):
    list_display = ['daya', 'tarif']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 
                    'first_name',
                    'last_name', 
                    'email',
                    'is_active',
                    'is_staff',
                    'is_superuser',
        	    ]
    list_filter = [
        ('is_active', admin.BooleanFieldListFilter),        
        ('is_superuser', admin.BooleanFieldListFilter),        
        ('is_staff', admin.BooleanFieldListFilter),        
    ]
    search_fields = [
        'username',
    ]


@admin.register(Months)
class MonthsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Uses)
class UsesAdmin(admin.ModelAdmin):
    list_display = [
        'custommer',
        'month',
        'year',
        'meter_start',
        'meter_end',
    ]
    search_fields = ['custommer']
    list_filter = [
        ('custommer', admin.RelatedOnlyFieldListFilter),
    ]


@admin.register(Tagihan)
class TagihanAdmin(admin.ModelAdmin):
    list_display = ['custommer', 'uses', 'month', 'year', 'sum_meter', 'status']
    search_fields = [
        ('custommer', admin.RelatedOnlyFieldListFilter),
        ('uses', admin.RelatedOnlyFieldListFilter),
        ('month', admin.RelatedOnlyFieldListFilter),
    ]

@admin.register(PayMent)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        'tagihan',
        'date_pay',
        'biaya_admin',
        'sumPayment',
    ]
    ordering = ['id']
    search_fields = ['custummer']
