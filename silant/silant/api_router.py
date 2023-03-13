from rest_framework import routers

from api.views import (ModMashinsGViewSet, ModMotorGViewSet, ModTransmissionGViewSet,
                       ModDriveBridgeGViewSet, ModControllBridgeGViewSet, RecoveryMethodGViewSet,
                       NatureRefusalGViewSet, FailureNodeReferenceViewSet, VidTOGViewSet, MashinsViewSet,
                       TOViewSet, ComplaintViewSet, ClientGViewSet, SersviceViewSet)

router = routers.DefaultRouter()

router.register('model_mashins', ModMashinsGViewSet)
router.register('motors', ModMotorGViewSet)
router.register('transmissions', ModTransmissionGViewSet)
router.register('drivebridge', ModDriveBridgeGViewSet)
router.register('controllbridge', ModControllBridgeGViewSet)
router.register('recoverymethod', RecoveryMethodGViewSet)
router.register('naturerefusal', NatureRefusalGViewSet)
router.register('failurenode', FailureNodeReferenceViewSet)
router.register('vidTO', VidTOGViewSet)
router.register('mashins', MashinsViewSet)
router.register('TO', TOViewSet)
router.register('complaint', ComplaintViewSet)
router.register('client', ClientGViewSet)
router.register('service', SersviceViewSet)
