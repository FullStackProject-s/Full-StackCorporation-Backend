from user.tests.utils import create_profiles


class CreateEmployeesTestCaseMixin:
    def _create_employee_response(
            self,
            employee_count,
            employee_url,
            **kwargs
    ):
        profile_pk = employee_count + abs(hash("create"))
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
            **kwargs
    ):
        return self.client.patch(
            employee_url,
            data=self.__configurate_update_json(
                employee_count,
                **kwargs
            )
        )

    def _put_employee_response(
            self,
            employee_count,
            employee_url,
            **kwargs

    ):
        return self.client.put(
            employee_url,
            data=self.__configurate_update_json(
                employee_count,
                **kwargs
            )
        )

    def __configurate_update_json(
            self,
            employee_count,
            **kwargs
    ):
        profile_pk = employee_count + abs(hash("put"))
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
