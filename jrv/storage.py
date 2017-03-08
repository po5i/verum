from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

class StaticStorage(S3BotoStorage):
#    location = settings.STATICFILES_LOCATION
    custom_domain = settings.AWS_S3_CUSTOM_DOMAIN
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION
    custom_domain = settings.AWS_S3_CUSTOM_DOMAIN_UPLOADS
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME_UPLOADS
    
    #https://github.com/sehmaschine/django-filebrowser/issues/40
    
    def isfile(self, name):
        return self.exists(name)

    def path(self, name):
        return name

    def isdir(self, name):
        # That's some inefficient implementation...
        # If there are some files having 'name' as their prefix, then
        # the name is considered to be a directory
        if not name: # Empty name is a directory
            return True

        if self.isfile(name):
            return False

        name = self._normalize_name(self._clean_name(name))
        dirlist = self.bucket.list(self._encode_name(name))

        # Check whether the iterator is empty
        for item in dirlist:
            return True
        return False

    def makedirs(self, name):
        pass

    def rmtree(self, name):
        name = self._normalize_name(self._clean_name(name))
        dirlist = self.bucket.list(self._encode_name(name))
        for item in dirlist:
            item.delete()
    
