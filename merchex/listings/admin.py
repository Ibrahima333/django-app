from django.contrib import admin

# Register your models here.
from listings.models import Band, Listing

# pour personnaliser l’affichage dans le site d'admin  (par exemple afficher name au lieu de Band object (1) et ajouter des colonnes utiles)
class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste
    
    
admin.site.register(Band, BandAdmin)
# nous modifions cette ligne, en ajoutant un deuxième argument le premier indiquant a l'interface admin 
# de prendre en compte notre model Band et le deuxieme indiquand la modification de l'affichage
admin.site.register(Listing)
