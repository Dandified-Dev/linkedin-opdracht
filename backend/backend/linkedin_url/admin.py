from django.contrib import admin
from .models import Url, Profile, Experience, Education, Skill
# Register your models here.
admin.site.register(Url)
admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
