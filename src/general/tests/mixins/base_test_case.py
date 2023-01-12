from django.urls import reverse

from rest_framework import status


class ListObjectsMixin:
    def _test_get_all_objects(self):
        response = self.client.get(self.all_objects_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.json()),
            self.number_of_objects
        )
        return response


class RetrieveObjectsMixin:
    def _test_retrieve_object(self):
        obj = getattr(self, f'obj_{self.default_object_number}')
        pk = obj.pk
        response = self.client.get(
            reverse(self.retrieve_object_url, kwargs={'pk': pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        response_json = response.json()

        self.assertEqual(
            response_json,
            self.serializer_class(obj).data
        )
        return response


class DeleteObjectsMixin:

    def _test_delete_object(self):
        obj = getattr(self, f'obj_{self.default_object_number}')
        pk = obj.pk
        response = self.client.delete(
            reverse(self.delete_object_url, kwargs={'pk': pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            self.model_class.objects.filter(pk=pk).exists(),
            False
        )
        return response


class CreateObjectsMixin:
    def _test_create_object(self, json: dict):
        response = self.client.post(
            self.create_object_url,
            data=json
        )
        response_json = response.json()

        pk = response_json['pk']

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            self.model_class.objects.filter(pk=pk).exists(),
            True
        )
        self.assertEqual(
            response_json,
            self.serializer_class(
                self.model_class.objects.get(pk=pk)
            ).data
        )
        return response


class UpdateObjectsMixin:
    def _test_put_object(self, json: dict):
        obj = getattr(self, f'obj_{self.default_object_number}')

        pk = obj.pk

        response = self.client.put(
            reverse(self.update_object_url, kwargs={'pk': pk}),
            data=json
        )
        response_json = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json,
            self.serializer_class(
                self.model_class.objects.get(pk=pk)
            ).data,
        )
        return response

    def _test_patch_object(self, json: dict):
        obj = getattr(self, f'obj_{self.default_object_number}')

        pk = obj.pk

        response = self.client.patch(
            reverse(self.update_object_url, kwargs={'pk': pk}),
            data=json
        )
        response_json = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json,
            self.serializer_class(
                self.model_class.objects.get(pk=pk)
            ).data,
        )
        return response
