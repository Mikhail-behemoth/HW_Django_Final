from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class RecipeFavorShopListViewSet(mixins.CreateModelMixin,
                                 mixins.DestroyModelMixin,
                                 mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin,
                                 viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['recipe'] = kwargs.get('recipe_id')
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data))

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(self.Meta.model,
                                     user=request.user.id,
                                     recipe=kwargs.get('recipe_id'))
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
