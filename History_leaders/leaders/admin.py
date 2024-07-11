from django.contrib import admin
from .models import Country, Leader, Trait

# Register your models here.
admin.site.register(Country)
admin.site.register(Trait)

#@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'lifetime')
    list_filter = ('country', 'traits')
    search_fields = ('name',)
    filter_horizontal = ('traits',)

admin.site.register(Leader, LeaderAdmin)