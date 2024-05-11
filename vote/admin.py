from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(HallChairmanVote)
admin.site.register(ViceHallChairmanVote)
admin.site.register(GeneralSecretaryVote)
admin.site.register(FinancialSecretaryVote)
admin.site.register(InformationMinisterVote)
admin.site.register(InternalAffairsAndDefenseMinisterVote)
admin.site.register(HealthMinisterVote)
admin.site.register(SportMinisterVote)
admin.site.register(SocialAndWelfareMinisterVote)
admin.site.register(StudentRepresentativeCouncilVote)