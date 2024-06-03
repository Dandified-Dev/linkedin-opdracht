from ninja import NinjaAPI
from linkedin_url.models import Url, Profile, Experience, Education, Skill
from linkedin_url.schemas import UrlSchema
from linkedin_api import Linkedin
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
from django.http import JsonResponse


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

@app.post("urls/", response=UrlSchema)
def create_url(request, payload: UrlSchema):


    linkedin_url = payload.url  # Access the URL string field
    parsed_url = urlparse(linkedin_url)
    # Extract the last segment of the path
    profile_id = parsed_url.path.strip('/').split('/')[-1]
    print(profile_id)
    data = linkedin_api.get_profile(profile_id)
    first_name = data['firstName']
    last_name = data['lastName']
    headline = data['headline']
    experience = data['experience']
    education = data['education']
    skills = data['skills']

    URL = None

    if Url.objects.filter(url=payload.url).exists():
        URL = Url.objects.get(url=payload.url)
    else: 
        # Assuming payload.url is a valid URL string
        URL = Url.objects.create(url=payload.url)
        Profile.objects.create(url=URL, first_name=first_name, last_name=last_name, headline=headline)

        for exp in experience:
            title = exp.get('title', '')  # Handling missing title field
            company_name = exp.get('companyName')  # Handling missing companyName field
            location_name = exp.get('locationName', '')
            start_dates = exp['timePeriod']['startDate']
            end_dates = exp['timePeriod'].get('endDate', None)  # Handling missing endDate field

            Experience.objects.create(
                profile=Profile.objects.get(url=URL),
                title=title,
                company=company_name,
                location=location_name,
                start_date=start_dates,
                end_date=end_dates
            )


        for edu in education:
            Education.objects.create(
                profile=Profile.objects.get(url=URL),
                school=edu.get('schoolName', ''),
                degree=edu.get('degreeName', ''),
                field_of_study=edu.get('fieldOfStudy', ''),
                start_date=edu['timePeriod']['startDate'].get('year', ''),  # Parsing start date year
                end_date=edu['timePeriod'].get('endDate', {}).get('year', '')  # Parsing end date year or None
            )

        for skill in skills:
            Skill.objects.create(profile=Profile.objects.get(url=URL), skill_name=skill['name'])



    return URL
