from django.contrib import admin
from .models import (
    TwitterAccount ,
    AccountRecord
    )

# Register your models here.


admin.site.register(TwitterAccount)
admin.site.register(AccountRecord)


