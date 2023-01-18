from django.urls import reverse
from rest_framework import status


class DeleteObjectsPermsMixin:
    def _test_delete_object_perms(self):
        obj = getattr(self, f'obj_{self.default_changed_object_number}')

        pk = obj.pk
        response = self.client.delete(
            reverse(self.delete_object_url, kwargs={'pk': pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
        self.assertEqual(
            self.model_class.objects.filter(pk=pk).exists(),
            True
        )


class UpdateObjectsPermsMixin:

    def _test_put_object_perms(self):
        obj = getattr(self, f'obj_{self.default_changed_object_number}')

        pk = obj.pk
        response = self.client.put(
            reverse(self.update_object_url, kwargs={'pk': pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def _test_patch_object_perms(self):
        obj = getattr(self, f'obj_{self.default_changed_object_number}')

        pk = obj.pk
        response = self.client.patch(
            reverse(self.update_object_url, kwargs={'pk': pk})
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
