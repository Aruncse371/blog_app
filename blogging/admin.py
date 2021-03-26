from django.contrib import admin
from blogging.models import Details
from blogging.models import Login 
from blogging.models import Data
from blogging.models import Gender
# Register your models here.
admin.site.register(Details)
admin.site.register(Login)
admin.site.register(Data)
admin.site.register(Gender)
