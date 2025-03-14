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

    def list(self, request, *args, **kwargs):
        data = request.query_params  # Récupération des paramètres GET

        # Création dynamique avec des valeurs reçues (sinon valeurs par défaut)
        first_name = data.get("first_name", "Jon")
        last_name = data.get("last_name", "Doe")
        email = data.get("email", "example@example.com")
        phone_number = data.get("phone_number", "1234567890")
        date_of_birth = data.get("date_of_birth", "2000-01-01")
        address = data.get("address", "123 rue Exemple")

        # Création d'une nouvelle instance dans la DB
        new_instance = Abantu.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            address=address
        )

        time.sleep(5)  # Pause pour simuler un délai

        # Mise à jour dynamique de l'instance créée :
        # Pour chaque champ fourni, on ajoute " updated" à la valeur initiale
        updated_fields = {}
        for field in ["first_name", "last_name", "email", "phone_number", "address"]:
            if data.get(field):
                updated_fields[field] = data[field] + " updated"
        
        for key, value in updated_fields.items():
            setattr(new_instance, key, value)
        new_instance.save()  # Sauvegarde de la mise à jour

        time.sleep(5)  # Nouvelle pause pour la simulation

        # Récupération des 100 premiers éléments de la table Abantu
        queryset = Abantu.objects.all()[:100]
        serializer = AbantuSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
