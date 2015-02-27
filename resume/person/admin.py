from django.contrib import admin

from person.models import Person, Education, Previous, Branch, Profession, Region
# Register your models here.

class PersonEducationInline(admin.StackedInline):
    model = Education
    extra = 2

class PersonPreviousInline(admin.StackedInline):
    model = Previous
    extra = 2

class PersonAdmin(admin.ModelAdmin):
    fields = [ 'person_last_name','person_name','person_father_name','person_branch','person_profession',
               'person_birthday', 'person_region','person_city','person_position','person_phone_number','person_email',
               'person_skills','person_username']
    list_display = ['__unicode__','person_position','person_timestamp', 'person_updated']
    inlines = [PersonEducationInline, PersonPreviousInline]
    list_filter = ['person_timestamp']

class RegionAdmin(admin.ModelAdmin):
    fields = ['region']
    list_display = ['region']

class ProfessionBranch(admin.StackedInline):
    model = Profession
    extra = 5


class BranchAdmin(admin.ModelAdmin):
    fields = ['branch']
    list_display = ['branch']
    inlines = [ProfessionBranch]


admin.site.register(Person, PersonAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Branch, BranchAdmin)