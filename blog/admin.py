from django.contrib import admin
from blog.models import Blog, Contact


# Register your models here.

class blogadmin(admin.ModelAdmin):
    list_display=('title', 'desc')
 
admin.site.register(Blog, blogadmin)
admin.site.register(Contact)
#class BlogAdmin(admin.ModelAdmin):
 #   class Media:
  #      css = {
   #         "all":("css/main.css",)
    #    }
        
     #   js = ("js/blog.js",)
     

# Register your models here.
     