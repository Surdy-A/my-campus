from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Instructor)
admin.site.register(Link)




# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('title', 'instructor')




