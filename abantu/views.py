import time
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from .models import Abantu
from .serializers import AbantuSerializer
from rest_framework.permissions import AllowAny

class AbantuViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Abantu.objects.all()
    serializer_class = AbantuSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        x = Abantu.objects.create(
            first_name="guymi",
            last_name="IGICOCORO",
            email="guymi.igicocoro@gmail.com",
            phone_number="68381368",
            address="Kinindo"
        )

        time.sleep(5)

        fields_to_update = ["first_name", "last_name", "email", "phone_number", "address"]

        for field in fields_to_update:
            old_value = getattr(x, field) 
            existing_updates = Abantu.objects.filter(**{f"{field}__startswith": f"{old_value} updated"}).count()

            if existing_updates > 0:
                setattr(x, field, f"{old_value} updated {existing_updates + 1}")
            else:
                setattr(x, field, f"{old_value} updated")

        x.save()

        time.sleep(5)
    
        abantu = Abantu.objects.all()[:100]
        serializer = AbantuSerializer(abantu, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


