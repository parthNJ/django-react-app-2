from rest_framework import routers
from .api import UserProgramViewset, ProgramViewset, PurchasedProgramViewset

router = routers.DefaultRouter()
router.register('api/userProgram', UserProgramViewset, 'module')
router.register('api/program', ProgramViewset, 'module')
router.register('api/purchased-program', PurchasedProgramViewset, 'module')


urlpatterns = router.urls