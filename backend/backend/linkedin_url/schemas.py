from ninja import ModelSchema
from linkedin_url.models import Url

class UrlSchema(ModelSchema):
    class Meta:
        model = Url
        fields = '__all__'

class ProfileSchema(ModelSchema):
    class Meta:
        model = Url
        fields = '__all__'

class ExperienceSchema(ModelSchema):
    class Meta:
        model = Url
        fields = '__all__'

class EducationSchema(ModelSchema):
    class Meta:
        model = Url
        fields = '__all__'

class SkillSchema(ModelSchema):
    class Meta:
        model = Url
        fields = '__all__'