from __future__ import unicode_literals

from django.db import models

class Guest(models.Model):
    name= models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=200)

def upload_avatar_to(instance, filename):
    import os
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'profiles/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )

    
class GuestPassport(models.Model):
	key = models.ForeignKey(Guest)
	passportphoto= models.ImageField(upload_to = upload_avatar_to, default = 'static/none.jpg')
    

  