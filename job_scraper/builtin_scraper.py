from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from job_scraper.excel_writer import write_to_excel
import os
import time
import requests

def get_with_retries(url, max_retries=3, delay=5):
    """Fetch a URL with retries in case of failure."""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response
            else:
                print(f"Attempt {attempt + 1}: Received status code {response.status_code}")
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1}: Error fetching {url} - {e}")
        time.sleep(delay)
    print(f"Failed to fetch {url} after {max_retries} retries.")
    return None

def scrape_builtin_jobs(keywords):
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    # Read the list of base URLs from the .env file
    base_urls = os.getenv("BUILTIN_BASE_URLS", "").split(",")
    jobs = []

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    for base_url in base_urls:
        base_url = base_url.strip()  # Remove any leading/trailing whitespace
        if not base_url:
            continue

        for keyword in keywords:
            url = f"{base_url}?search={keyword}"
            print(f"Fetching URL: {url}")
            driver.get(url)
            time.sleep(5)  # Wait for the page to load

            # Save the rendered HTML to a file for debugging
            soup = BeautifulSoup(driver.page_source, "html.parser")
            file_path = os.path.join(output_dir, f"debug_{keyword.replace(' ', '_')}.txt")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(soup.prettify())
            print(f"Saved rendered HTML content to {file_path}")

            # Select job cards
            for card in soup.select(".job-bounded-responsive"):  # Update this selector if necessary
                title_element = card.select_one("h2 a")  # Selector for job title
                company_element = card.select_one(".left-side-tile-item-2 a")  # Selector for company name
                link_element = card.select_one("h2 a")  # Selector for job link

                if title_element and company_element and link_element:
                    job_link = f"https://builtin.com{link_element['href']}"  # Construct full job link

                    # Fetch job description from the job detail page
                    job_description = fetch_job_description(job_link)

                    # Extract additional parameters if available
                    location_element = card.select_one(".font-barlow.text-gray-04")  # Selector for location
                    salary_element = card.select_one(".fs-xs.fw-bold.text-gray-04")  # Selector for salary
                    level_element = card.select_one(".fs-xs.text-gray-04")  # Selector for job level

                    job = {
                        "title": title_element.text.strip(),
                        "company": company_element.text.strip(),
                        "link": job_link,
                        "job_description": job_description,
                        "location": location_element.text.strip() if location_element else "Not Specified",
                        "salary": salary_element.text.strip() if salary_element else "Not Specified",
                        "level": level_element.text.strip() if level_element else "Not Specified",
                        "source": base_url,
                        "applied_status": "Not Applied",
                        "applied_date": "",
                        "follow_up_date": "",
                        "cold_email_contacts": "",
                        "tech_to_study": "",
                        "resume_used": ""
                    }
                    jobs.append(job)

                    # Write the job to Excel immediately
                    write_to_excel([job], output_path="output/results.xlsx")

    driver.quit()
    print(f"Total jobs scraped: {len(jobs)}")
    return jobs


def fetch_job_description(job_link):
    """Fetch the job description from the job detail page."""
    response = get_with_retries(job_link)
    if not response:
        print(f"Failed to fetch job description from {job_link}")
        return "Not Available"

    soup = BeautifulSoup(response.text, "html.parser")
    description_element = soup.select_one(".fs-sm.fw-regular.text-gray-04")  # Selector for job description
    return description_element.text.strip() if description_element else "Not Available"