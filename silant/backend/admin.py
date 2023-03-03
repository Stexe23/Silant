from django.contrib import admin

from users.models import CustomUser
from .models import (ModMotorG, ModTransmissionG, Mashins, ModMashinsG, ModDriveBridgeG,
                     ModControllBridgeG, RecoveryMethodG, Complaint, NatureRefusalG,
                     ClientG, Sersvice, VidTOG, TO)
# Register your models here.

admin.site.register(ModMotorG)
admin.site.register(ModDriveBridgeG)
admin.site.register(ModTransmissionG)
admin.site.register(ModMashinsG)
admin.site.register(ModControllBridgeG)

admin.site.register(Mashins)
admin.site.register(RecoveryMethodG)
admin.site.register(Complaint)
admin.site.register(NatureRefusalG)
admin.site.register(VidTOG)
admin.site.register(TO)

admin.site.register(ClientG)
admin.site.register(Sersvice)

admin.site.register(CustomUser)
