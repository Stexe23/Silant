from rest_framework import routers

from ..api.views import (ModMashinsGViewSet, ModMotorGViewSet, ModTransmissionGViewSet, ModDriveBridgeGViewSet,
                         ModControllBridgeGViewSet, RecoveryMethodGViewSet, NatureRefusalGViewSet,
                         FailureNodeReferenceViewSet, VidTOGViewSet, MashinsViewSet, TOViewSet,
                         ComplaintViewSet, ClientGViewSet, SersviceViewSet)


router = routers.DefaultRouter()

router.register('Модели машин', ModMashinsGViewSet)
router.register('Модели моторов', ModMotorGViewSet)
router.register('Модели трансмиссий', ModTransmissionGViewSet)
router.register('Модели ведущего моста', ModDriveBridgeGViewSet)
router.register('Модели управляемого моста', ModControllBridgeGViewSet)
router.register('Способ восстановления', RecoveryMethodGViewSet)
router.register('Описание отказа', NatureRefusalGViewSet)
router.register('Узел отказа', FailureNodeReferenceViewSet)
router.register('Вид технического обслуживания', VidTOGViewSet)
router.register('Машины', MashinsViewSet)
router.register('Технические обслуживания', TOViewSet)
router.register('Рекламации', ComplaintViewSet)
router.register('Клиенты', ClientGViewSet)
router.register('Сервисные компании', SersviceViewSet)

