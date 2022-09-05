from django.contrib import admin
from .models import artical,bookreview,somajsongsker,songbad,itihash,law,politics,interview,Personality,Islamic,Bibidh,blog,Recentworld,BrakingNews,ElectedPost
from django.contrib.auth.models import Group

admin.site.site_header='Resurrection-BD'

admin.site.unregister(Group)
admin.site.register(artical)
admin.site.register(bookreview)
admin.site.register(somajsongsker)
admin.site.register(songbad)
admin.site.register(itihash)
admin.site.register(law)
admin.site.register(politics)
admin.site.register(interview)
admin.site.register(Personality)
admin.site.register(Islamic)
admin.site.register(Bibidh)
admin.site.register(blog)
admin.site.register(Recentworld)
admin.site.register(ElectedPost)
admin.site.register(BrakingNews)
# Register your models here.
