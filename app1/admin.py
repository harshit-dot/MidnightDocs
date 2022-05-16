from django.contrib import admin

# Register your models here.
from .models import contact
from .models import blogpost
from .models import appointment
from .models import image
admin.site.register(appointment)
admin.site.register(contact)
admin.site.register(blogpost)
admin.site.register(image)
