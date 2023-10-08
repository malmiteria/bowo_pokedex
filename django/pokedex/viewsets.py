from rest_framework import filters, viewsets
from pokedex.models import Pokemon
from pokedex.serializers import PokemonSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "type1", "type2"]
