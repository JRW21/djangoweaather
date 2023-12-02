#views.py file
from django.shortcuts import render

def home(request):
    import json
    import requests #will need to install for each new django project
    
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        #return render(request, 'home.html', {'zipcode':zipcode})
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=158162B3-4494-4FC3-B367-1454EB8B7F93")

        try:
            api = json.loads(api_request.content)#This calls json to load data from api_request variable
        except Exception as e:
            api= "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0-50) Air quality is conidered satisfactory. No or little risk"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description="(51-100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description="(101-150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone"
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description="(151-200) Everyone may begin to expereinece health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description="(201-300) Health alert: everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description="(301-500) Health warnings of emergency conditions. The entire population is more likely to be affected."
            category_color = "hazardous" 
            
        return render(request, 'home.html', {'api':api,'category_description' : category_description,
                                                'category_color' : category_color})
    else:
    
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=60102&distance=25&API_KEY=158162B3-4494-4FC3-B367-1454EB8B7F93")

        try:
            api = json.loads(api_request.content)#This calls json to load data from api_request variable
        except Exception as e:
            api= "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0-50) Air quality is conidered satisfactory. No or little risk"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description="(51-100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description="(101-150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone"
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description="(151-200) Everyone may begin to expereinece health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description="(201-300) Health alert: everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description="(301-500) Health warnings of emergency conditions. The entire population is more likely to be affected."
            category_color = "hazardous" 
                
            
        return render(request, 'home.html', {'api':api,'category_description' : category_description,
                                                'category_color' : category_color})#{} passes in python dictionary, can acess api by using 'api'
# This is the api key for airnow https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=60102&distance=25&API_KEY=158162B3-4494-4FC3-B367-1454EB8B7F93
def about(request):
    return render(request, 'about.html', {})#{} passes in python dictionary
