from django.http import Http404


class MeAPIViewMixin:
    def _get_me_object_or_404(self):
        if obj := self.get_queryset().filter(
                profile__user=self.request.user):
            return obj.first()
        raise Http404
