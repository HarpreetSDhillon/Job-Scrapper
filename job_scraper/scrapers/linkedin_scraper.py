from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from job_scraper.config import LINKEDIN_EMAIL, LINKEDIN_PASSWORD

def scrape_linkedin_jobs(keywords):
    options = Options()
    options.add_argument("--headless")  # Use headless mode for production
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    driver = webdriver.Chrome(options=options)

    try:
        # Log in to LinkedIn
        driver.get("https://www.linkedin.com/login")
        driver.find_element(By.ID, "username").send_keys(LINKEDIN_EMAIL)
        driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(3)  # Wait for login to complete

        jobs = []

        for keyword in keywords:
            try:
                print(f"Scraping jobs for keyword: {keyword}")
                driver.set_page_load_timeout(60)  # Increase timeout
                driver.get(f"https://www.linkedin.com/jobs/search/?keywords={keyword}")
                time.sleep(5)  # Wait for the page to load

                cards = driver.find_elements(By.CLASS_NAME, "base-card")
                for card in cards[:10]:  # Limit to top 10 jobs
                    try:
                        title = card.find_element(By.CLASS_NAME, "base-search-card__title").text
                        company = card.find_element(By.CLASS_NAME, "base-search-card__subtitle").text
                        link = card.find_element(By.TAG_NAME, "a").get_attribute("href")

                        jobs.append({
                            "title": title.strip(),
                            "company": company.strip(),
                            "link": link,
                            "source": "linkedin.com",
                            "applied_status": "Not Applied",
                            "applied_date": "",
                            "follow_up_date": "",
                            "cold_email_contacts": "",
                            "tech_to_study": "",
                            "resume_used": ""
                        })
                    except NoSuchElementException:
                        continue
            except TimeoutException:
                print(f"Timeout while loading jobs for keyword: {keyword}")
                continue

    except Exception as e:
        print(f"Error during LinkedIn scraping: {e}")
    finally:
        driver.quit()

    return jobs