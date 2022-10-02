import uuid
from typing import Any

from django.db import models
from rest_framework import permissions, status
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Relation, Tag
from .serializers import RelationSerializer, TagSerializer


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


# =============================================================================


class TagViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet,
    DestroyModelMixin,
    UpdateModelMixin,
):
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tag.objects.all()
    lookup_field = "id"

    def get_queryset(self) -> models.QuerySet[Tag]:
        assert isinstance(self.request.user.id, uuid.UUID)
        return self.queryset.filter(author=self.request.user)

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(author=request.user)

        return Response(
            {"status": "success", "message": "Tag created successfully."},
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data),
        )
