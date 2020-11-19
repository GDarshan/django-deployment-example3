from django.contrib import admin
from testapp.models import Topic,Webpage,AccessRecord

class TopicAdmin(admin.ModelAdmin):
      list_display=['top_name']

class WebpageAdmin(admin.ModelAdmin):
      list_display=['topic','name','url']

class AccessRecordAdmin(admin.ModelAdmin):
      list_display=['name','date']


admin.site.register(AccessRecord,AccessRecordAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Webpage,WebpageAdmin)
