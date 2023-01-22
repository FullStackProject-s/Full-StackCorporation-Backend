from io import BytesIO

from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from rest_framework import status


class ImageUploadMixin:

    def _test_image_upload(self, image_field_name):
        obj = getattr(self, f'obj_{self.default_object_number}')

        pk = obj.pk

        bts = BytesIO()
        img = Image.new('RGB', (1, 1))
        img.save(bts, 'jpeg')

        tmp_file = SimpleUploadedFile(
            name="file.jpg",
            content=bts.getvalue(),
            content_type="image/jpg"
        )

        response = self.client.post(
            reverse(
                self.upload_obj_image_url, kwargs={'pk': pk}
            ),
            data={image_field_name: tmp_file},
            format='multipart'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_202_ACCEPTED
        )
