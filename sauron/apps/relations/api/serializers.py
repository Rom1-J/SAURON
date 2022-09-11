from rest_framework import serializers

from ..models import Relation


class RelationSerializer(serializers.ModelSerializer[Relation]):
    class Meta:
        model = Relation
        fields = [
            "author",
            "first_name",
            "last_name",
            "relations",
            "tags",
            "attachments",
            "links",
        ]
        read_only_fields = ["author"]
