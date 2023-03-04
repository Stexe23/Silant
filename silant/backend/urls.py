from django.urls import path, include


from silant.backend.api_router import router


urlpatterns = [
    path('api/', include(router.urls))
]
