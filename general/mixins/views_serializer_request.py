class ViewsSerializerValidateRequestMixin:
    def _validate_request(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return serializer
