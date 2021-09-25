from rest_framework import routers
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from apps.chat.views import ConversionViewSet, ChatViewSet
from apps.store.views import StoreViewSet, DiscountCodeViewSet
from apps.account.views import OperatorViewSet, ClientViewSet

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"user", UserViewSet)
router.register(r"conversation", ConversionViewSet)
router.register(r"chat", ChatViewSet)
router.register(r"store", StoreViewSet)
router.register(r"discount", DiscountCodeViewSet)
router.register(r"operator", OperatorViewSet)
router.register(r"client", ClientViewSet)
