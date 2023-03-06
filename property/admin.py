from django.contrib import admin

from .models import Flat, Grievance, Owner


# class FlatInline(admin.TabularInline):
#     model = Flat.owner.through
#     raw_id_fields = ('owner', 'flat', )


class FlatModelAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at', )
    list_display = ('address', 'price', 'new_building', 'construction_year',
                    'town', 'owners_phonenumber', 'owner_pure_phone')
    list_editable = ('new_building', )
    list_filter = ('new_building', )
    raw_id_fields = ('likes', )
    # inlines = [
    #     FlatInline,
    # ]


class ModelAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', )


admin.site.register(Flat, FlatModelAdmin)
admin.site.register(Grievance, ModelAdmin)
admin.site.register(Owner, ModelAdmin)
