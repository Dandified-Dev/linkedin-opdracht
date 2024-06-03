from ninja import NinjaAPI
from linkedin_url.models import Url
from linkedin_url.schemas import UrlSchema
from linkedin_api import Linkedin
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

load_dotenv()

app = NinjaAPI()

@app.get("urls/", response=list[UrlSchema])
def get_urls(request):
    return Url.objects.all()



linkedin_api = Linkedin(os.getenv('email'), os.getenv('password'))

@app.get("/profile/{profile_id}")
def profile(request, profile_id: str):
        profile_data = linkedin_api.get_profile(profile_id)
        return profile_data


@app.get("/profiles")
def profile(request):
    links = Url.objects.all()
    data = []
    for link in links:
        linkedin_url = link.Url  # Access the URL string field
        parsed_url = urlparse(linkedin_url)

        # Extract the last segment of the path
        profile_id = parsed_url.path.strip('/').split('/')[-1]
        print(profile_id)
        
        try:
            profile_data = linkedin_api.get_profile(profile_id)
            data.append(profile_data)
        except Exception as e:
            print(f"Failed to get profile for ID {profile_id}: {e}")
            continue
    
    return data

@app.post("urls/", response=UrlSchema)
def create_url(request, payload: UrlSchema):
    return Url.objects.create(**payload.dict())