from django.contrib import admin

from .models import Flat, Grievance, Owner


# class FlatInline(admin.TabularInline):
#     model = Flat.owner.through
#     raw_id_fields = ('owner', 'flat', )


@admin.register(Flat)
class FlatModelAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at', )
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building', )
    list_filter = ('new_building', )
    raw_id_fields = ('likes', )
    # inlines = [
    #     FlatInline,
    # ]


@admin.register(Grievance, Owner)
class ModelAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', )
