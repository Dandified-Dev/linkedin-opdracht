from ninja import ModelSchema
from linkedin_url.models import Url

class UrlSchema(ModelSchema):
    class Meta:
        model = Url
        fields = '__all__'