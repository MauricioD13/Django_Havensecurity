from django.contrib import admin
from users.models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user')
    list_display_links = ('pk', 'user')
    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name'
    )
    list_filter = (
        'user__is_active',
        'created',
        'modified'
    )

    fieldsets = (
        ('Profile',
            {
                'fields': (('user', 'created', 'modified'),),
            }),
    )
    readonly_fields = ('created', 'modified')

    """
    Permite editar el campo -> Formulario
    list_editable = ('')
    """

class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users"""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',


    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)