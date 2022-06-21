from django.contrib import admin

from neighbour.models import Business, NeighbourHood, Post

# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(Business)
admin.site.register(Post)
