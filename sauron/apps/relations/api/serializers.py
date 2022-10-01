from rest_framework import serializers

from ..models import Relation, Tag


class RelationSerializer(serializers.ModelSerializer[Relation]):
    class Meta:
        model = Relation
        fields = [
            "id",
            "author",
            "first_name",
            "last_name",
            "relations",
            "tags",
            "attachments",
            "links",
        ]
        read_only_fields = ["id", "author"]


class TagSerializer(serializers.ModelSerializer[Tag]):
    class Meta:
        model = Tag
        fields = ["id", "note", "name", "color", "uses"]
        read_only_fields = ["id", "uses"]
