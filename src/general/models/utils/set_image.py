from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.fields.files import ImageFieldFile

from general.utils import generate_avatar


def set_image_on_imagefield(
        *args,
        imagefield: ImageFieldFile,
):
    if hasattr(settings, 'TESTS_LAUNCHED'):
        if settings.TESTS_LAUNCHED:
            return
    img = generate_avatar(*args)

    img_name = f'{"".join([str(abs(hash(ele))) for ele in args])}.png'

    imagefield.save(
        img_name,
        InMemoryUploadedFile(
            img,
            None,
            img_name,
            'image/jpeg',
            img.tell,
            None
        )
    )
