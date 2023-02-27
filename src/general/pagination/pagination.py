from collections import OrderedDict

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomRelatedUrlPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        next_url = self.get_next_link()
        previous_url = self.get_previous_link()

        if next_url is not None:
            next_url = next_url.replace(
                self.request.build_absolute_uri().replace(
                    self.request.get_full_path(), ''), ''
            )
        if previous_url is not None:
            previous_url = previous_url.replace(
                self.request.build_absolute_uri().replace(
                    self.request.get_full_path(), ''), ''
            )

        return Response(OrderedDict([
            ('count', self.count),
            ('next', next_url),
            ('previous', previous_url),
            ('results', data)
        ]))
