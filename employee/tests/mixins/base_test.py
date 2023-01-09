from user.tests.utils import create_profiles


class CreateEmployeesTestCaseMixin:
    def _create_employee_response(
            self,
            employee_count,
            employee_url,
            keyword='create',
            **kwargs
    ):
        profile_pk = employee_count + abs(hash(keyword))
        profile = create_profiles(profile_pk, start=profile_pk)[0]
        json = {
            'profile': profile.pk,
            **kwargs
        }
        return self.client.post(
            employee_url,
            data=json
        )


class UpdateEmployeesTestCaseMixin:
    def _patch_employee_response(
            self,
            employee_count,
            employee_url,
            keyword='patch',
            **kwargs
    ):
        return self.client.patch(
            employee_url,
            data=self.__configurate_update_json(
                employee_count,
                keyword=keyword,
                **kwargs
            )
        )

    def _put_employee_response(
            self,
            employee_count,
            employee_url,
            keyword='put',
            **kwargs

    ):
        return self.client.put(
            employee_url,
            data=self.__configurate_update_json(
                employee_count,
                keyword=keyword,
                **kwargs
            )
        )

    def __configurate_update_json(
            self,
            employee_count,
            keyword='__configurate_update_json',
            **kwargs
    ):
        profile_pk = employee_count + abs(hash(keyword))
        profile = create_profiles(profile_pk, start=profile_pk)[0]
        return {
            "profile": profile.pk,
            **kwargs
        }


class CreateUpdateEmployeeTestCaseMixin(
    CreateEmployeesTestCaseMixin,
    UpdateEmployeesTestCaseMixin
):
    pass
