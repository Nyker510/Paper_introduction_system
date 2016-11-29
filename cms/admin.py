from django.contrib import admin
from cms.models import Paper, Report

'''
def toggle_recommended(modelAdmin, request, queryset):
    for paper in queryset.all():
        paper.recommended = True
        paper.save()

toggle_recommended.short_description = (u"Toggle Recommended")
'''

class PaperAdmin(admin.ModelAdmin):
    list_display = ('id',  'title',)
    list_display_links = ('id','title')
#    actions = [toggle_recommended]
admin.site.register(Paper, PaperAdmin)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'reporter','date',)
    list_display_links = ('id', 'reporter',)
#    actions = [toggle_recommended]
admin.site.register(Report, ReportAdmin)
