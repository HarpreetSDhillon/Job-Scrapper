import argparse
from job_scraper.scraper import scrape_jobs
from job_scraper.excel_writer import write_to_excel
from job_scraper.follow_up_checker import check_for_followups
from job_scraper.config import KEYWORDS
from job_scraper.model.scrapers.builtin_scraper import scrape_builtin_jobs
from job_scraper.model.scrapers.linkedin_scraper import scrape_linkedin_jobs

SCRAPER_MAP = {
    "default": scrape_jobs,
    "builtin": scrape_builtin_jobs,
    # "linkedin": scrape_linkedin_jobs,
}

def main():
    parser = argparse.ArgumentParser(description="Job Scraper CLI")
    parser.add_argument("--site", type=str, help="Comma-separated list of sites to scrape (e.g. builtin,linkedin)")
    parser.add_argument("--followup", action="store_true", help="Check for follow-up tasks")
    args = parser.parse_args()

    jobs = []

    if args.site:
        site_list = [s.strip() for s in args.site.split(",") if s.strip()]
        for site in site_list:
            scraper = SCRAPER_MAP.get(site)
            if scraper:
                print(f"Scraping jobs from {site}...")
                scraped = scraper(KEYWORDS) if site != "default" else scraper()
                jobs.extend(scraped)
                print(f"Scraped {len(scraped)} jobs from {site}.")
                write_to_excel(jobs)
            else:
                print(f"No scraper found for: {site}")

    if jobs:
        print(f"Writing {len(jobs)} jobs to Excel...")
        write_to_excel(jobs)

    if args.followup:
        print("Checking for follow-ups...")
        check_for_followups()

if __name__ == "__main__":
    main()