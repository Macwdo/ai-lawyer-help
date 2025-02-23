from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from http import HTTPMethod

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
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


class BaseModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    lookup_url_kwarg = "code"
    lookup_field = "code"

    nested_field = None
    nested_prefix = None
    parent_model = None

    def get_queryset(self):
        return self.queryset.order_by("-created_at")  # type: ignore

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        if self.nested_field and self.nested_prefix:
            kwarg = f"{self.nested_prefix}_{self.nested_field}"
            ctx[self.nested_prefix] = get_object_or_404(
                self.parent_model, code=self.kwargs[kwarg]
            )  # type: ignore

        return ctx
