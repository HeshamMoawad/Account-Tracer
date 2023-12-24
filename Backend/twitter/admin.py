from django.contrib import admin
from .models import (
    # TwitterAccount ,
    # AccountRecord ,
    Project ,
    Agent
    )

# Register your models here.

admin.site.register(Project)
admin.site.register(Agent)
# admin.site.register(TwitterAccount)
# admin.site.register(AccountRecord)


