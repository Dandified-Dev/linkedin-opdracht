from ninja import NinjaAPI

api = NinjaAPI()

from ninja import Schema

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    # Unauthenticated users don't have the following fields, so provide defaults.
    email: str = None
    first_name: str = None
    last_name: str = None

@api.get("/me", response=UserSchema)
def me(request):
    return request.user

from linkedin_api import Linkedin

# Authenticate using any Linkedin account credentials
apis = Linkedin('miwitiv261@jahsec.com', 'Test1234')

@api.get("/profile/{linkedin_id}")
def profile(request, linkedin_id: str):
    data = apis.get_profile(linkedin_id)
    return data

