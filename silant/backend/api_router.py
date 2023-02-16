from rest_framework import routers

from .views import (ModMotorGListCreate, ModTransmissionGListCreate, MashinsListCreate, ModMashinsGListCreate,
                    ModDriveBridgeGListCreate, ModControllBridgeGListCreate, RecoveryMethodGListCreate,
                    ClientGListCreate, ComplaintListCreate, NatureRefusalGListCreate, VidTOGListCreate,
                    TOListCreate, SersviceListCreate, UsersSilantListCreate)


router = routers.DefaultRouter()

router.register('modmotor', ModMotorGListCreate)
router.register('modtransmission', ModTransmissionGListCreate)
router.register('mashins', MashinsListCreate)
router.register('modmashins', ModMashinsGListCreate)
router.register('moddrivebridge', ModDriveBridgeGListCreate)
router.register('modcontrollbtidge', ModControllBridgeGListCreate)
router.register('recaoverymethod', RecoveryMethodGListCreate)
router.register('client', ClientGListCreate)
router.register('complain', ComplaintListCreate)
router.register('naturerefusal', NatureRefusalGListCreate)
router.register('vidto', VidTOGListCreate)
router.register('TO', TOListCreate)
router.register('service', SersviceListCreate)
router.register('userssilant', UsersSilantListCreate)
