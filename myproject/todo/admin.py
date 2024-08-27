

# Register your models here.

from django.contrib import admin
from .models import Todo, Category

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('IID', 'DEP_ID', 'MED_ID', 'KOD_SITE','ANALOG_ID', 'QTTY', 'RPRICE_SITE', 'RPRICE', 'SPRICE', 'SALLPRICE', 'VPRICE', 'REG_PRICE', 'date_stock', 'valid_date', 'VALID_PERIOD')
    list_filter = ('DEP_ID', 'MED_ID', 'KOD_SITE')
    search_fields = ('IID', 'MED_ID', 'KOD_SITE')


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'


admin.site.register(Todo, TodoAdmin)
admin.site.register(Category, CategoryAdmin)