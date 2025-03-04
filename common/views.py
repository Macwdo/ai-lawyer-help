from http import HTTPMethod

from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication


def auth_required(http_methods: list[HTTPMethod] = []):
    if len(http_methods) == 0:
        http_methods = [HTTPMethod.GET]

    def decorator(view_func):
        @api_view(http_methods)
        @authentication_classes([JWTAuthentication])
        @permission_classes([IsAuthenticated])
        def wrapped_view(request: Request, *args, **kwargs):
            return view_func(request, *args, **kwargs)

        return wrapped_view

    return decorator


class BaseAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class BaseGenericViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class BaseModelViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    BaseGenericViewSet,
):
    lookup_url_kwarg = "code"
    lookup_field = "code"

    nested_field = None
    nested_prefix = None
    parent_model = None  # type: ignore

    @property
    def nested_kwarg(self):
        return f"{self.nested_prefix}_{self.nested_field}"

    def get_queryset(self):
        filters = {}

        if self.nested_field and self.nested_prefix:
            nested_relation_filter = {
                f"{self.nested_prefix}__{self.nested_field}": self.kwargs[
                    self.nested_kwarg
                ]
            }
            filters.update(nested_relation_filter)

        queryset = self.queryset.filter(**filters).order_by(  # type: ignore
            "-created_at"
        )

        return queryset

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        if self.nested_field and self.nested_prefix:
            ctx[self.nested_prefix] = get_object_or_404(
                self.parent_model,  # type: ignore
                code=self.kwargs[self.nested_kwarg],  # type: ignore
            )

        return ctx
