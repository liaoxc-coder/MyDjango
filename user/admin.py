from django.contrib import admin
from user.models import CCITUser
from user.models import AClass, AStudent


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('uID', 'upwd', 'uname', 'uregistertime', 'uemail', 'ustatus')


admin.site.register(CCITUser, UserAdmin)


class ShowClass(admin.ModelAdmin):
    list_display = ('cID', 'cn', 'cETD', 'cadmin')


admin.site.register(AClass, ShowClass)


class ShowStudent(admin.ModelAdmin):
    list_display = ('sID', 'sname', 'sage', 'ssex', 'stel', 'smajor')


admin.site.register(AStudent, ShowStudent)
