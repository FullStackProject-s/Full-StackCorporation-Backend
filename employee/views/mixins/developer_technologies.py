from typing import Callable

from employee.models import Technologies
from general.services import response_many_to_many_api_views


class DeveloperTechnologiesRemoveUpdate:
    def _change_technologies(
            self,
            request,
            message: str,
            developer_method: Callable[[Technologies], None]
    ):
        tech_list = []

        for tech_name in self._validate_request(request).data[
            'technology_names'
        ]:
            if tech := Technologies.objects.filter(
                    technology_name=tech_name
            ).first():
                developer_method(tech)
                tech_list.append(tech.technology_name)
        return response_many_to_many_api_views(
            tech_list,
            message,
            'Tech not found'
        )
