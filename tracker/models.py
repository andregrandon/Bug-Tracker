from django.core.files.storage import FileSystemStorage
from django.conf import settings


image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/my_sell/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}my_sell/'.format(settings.MEDIA_URL),
)


def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/my_sell/picture/<filename>
    return u'picture/{0}'.format(filename)


class Goods(models.Model):
    pic = models.ImageField(upload_to=image_directory_path, storage=image_storage)
views:
