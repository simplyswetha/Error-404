import requests
from bs4 import BeautifulSoup

# URL of the LinkedIn profile you want to scrape
linkedin_url = "https://www.linkedin.com/in/namrata-mokshagundam-01538223b/"

# Send an HTTP GET request to the URL
response = requests.get(linkedin_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Scrape the desired attributes
    skills = [skill.text.strip() for skill in soup.find_all("span", class_="pv-skill-category-entity__name-text")]
    projects = [project.text.strip() for project in soup.find_all("li", class_="pv-entity__position-group-pager")]
    work_experience = [exp.text.strip() for exp in soup.find_all("section", class_="experience-section")]
    interests = [interest.text.strip() for interest in soup.find_all("section", class_="interests")]
    education = [edu.text.strip() for edu in soup.find_all("section", class_="education-section")]
    activity = [act.text.strip() for act in soup.find_all("section", class_="pv-profile-section__section-info")]

    # Print or use the scraped data as needed
    print("Skills:", skills)
    print("Projects:", projects)
    print("Work Experience:", work_experience)
    print("Interests:", interests)
    print("Education:", education)
    print("Activity:", activity)
else:
    print("Failed to retrieve the LinkedIn profile.")
