from ninja import NinjaAPI, Schema
from linkedin_url.models import Url, Profile, Experience, Education, Skill
from linkedin_url.schemas import UrlSchema
from linkedin_api import Linkedin
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
from django.http import JsonResponse
from typing import List



load_dotenv()
linkedin_api = Linkedin(os.getenv('email'), os.getenv('password'))
app = NinjaAPI()

@app.get("urls/", response=list[UrlSchema])
def get_urls(request):
    return Url.objects.all()

@app.get("/profile/{profile_id}")
def profile(request, profile_id: str):
        profile_data = linkedin_api.get_profile(profile_id)
        return profile_data



@app.get("/profiles")
def profile(request):
    profiles = Profile.objects.all()
    profile_data = []
    for profile in profiles:
        # Get the data for the Profile object
        profile_dict = profile.__dict__
        
        # Get the data for the related Url object
        url_data = profile.url.__dict__
        profile_dict['url'] = url_data['url']
        
        # Get the data for the related Experience objects
        experiences_data = list(profile.experience_set.values())
        profile_dict['experiences'] = experiences_data
        
        # Get the data for the related Education objects
        educations_data = list(profile.education_set.values())
        profile_dict['educations'] = educations_data
        
        # Get the data for the related Skill objects
        skills_data = list(profile.skill_set.values())
        profile_dict['skills'] = skills_data
        
        # Remove unnecessary fields
        del profile_dict['_state']
        del profile_dict['url_id']

        # Append the profile data to the list
        profile_data.append(profile_dict)
    
    return JsonResponse(profile_data, safe=False)

class UrlsPayload(Schema):
    url: List[str]

@app.post("urls/", response=List[UrlSchema])
def create_url(request, payload: UrlsPayload):
    processed_urls = []

    for linkedin_url in payload.url:
        parsed_url = urlparse(linkedin_url)
        profile_id = parsed_url.path.strip('/').split('/')[-1]
        data = linkedin_api.get_profile(profile_id)
        
        first_name = data.get('firstName', '')
        last_name = data.get('lastName', '')
        headline = data.get('headline', '')
        experience = data.get('experience', [])
        education = data.get('education', [])
        skills = data.get('skills', [])

        if Url.objects.filter(url=linkedin_url).exists():
            url_instance = Url.objects.get(url=linkedin_url)
        else:
            url_instance = Url.objects.create(url=linkedin_url)
            profile_instance = Profile.objects.create(url=url_instance, first_name=first_name, last_name=last_name, headline=headline)

            for exp in experience:
                title = exp.get('title', '')
                company_name = exp.get('companyName', '')
                location_name = exp.get('locationName', '')
                start_dates = exp['timePeriod']['startDate']
                end_dates = exp['timePeriod'].get('endDate', None)
                Experience.objects.create(
                    profile=profile_instance,
                    title=title,
                    company=company_name,
                    location=location_name,
                    start_date=start_dates,
                    end_date=end_dates
                )

            for edu in education:
                Education.objects.create(
                    profile=profile_instance,
                    school=edu.get('schoolName', ''),
                    degree=edu.get('degreeName', ''),
                    field_of_study=edu.get('fieldOfStudy', ''),
                    start_date=edu['timePeriod']['startDate'].get('year', ''),
                    end_date=edu['timePeriod'].get('endDate', {}).get('year', '')
                )

            for skill in skills:
                Skill.objects.create(profile=profile_instance, skill_name=skill['name'])

        processed_urls.append({"url": linkedin_url})

    return processed_urls
