import uuid
from typing import Any

from django.db import models
from rest_framework import permissions
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Relation
from .serializers import RelationSerializer


class RelationViewSet(
    RetrieveModelMixin, ListModelMixin, CreateModelMixin, GenericViewSet
):
    serializer_class = RelationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Relation.objects.all()
    lookup_field = "id"

    def get_queryset(self) -> models.QuerySet[Relation]:
        assert isinstance(self.request.user.id, uuid.UUID)
        return self.queryset.filter(author=self.request.user)

    def perform_create(  # type: ignore[override]
        self, serializer: RelationSerializer
    ) -> None:
        print("perform_create")

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        print("create")

        return Response()

    # =========================================================================

    def retrieve(
        self, request: Request, *args: Any, **kwargs: Any
    ) -> Response:
        print("retrieve")

        return Response()
