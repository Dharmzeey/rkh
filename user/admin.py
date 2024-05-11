from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(HallChairman)
admin.site.register(ViceHallChairman)
admin.site.register(GeneralSecretary)
admin.site.register(FinancialSecretary)
admin.site.register(InformationMinister)
admin.site.register(InternalAffairsAndDefenseMinister)
admin.site.register(HealthMinister)
admin.site.register(SportMinister)
admin.site.register(SocialAndWelfareMinister)
admin.site.register(StudentRepresentativeCouncil)