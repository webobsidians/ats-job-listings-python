# Scrape Job Listings from Greenhouse, Lever and Ashby Career Pages (Python and No-Code)

Many company career pages run on an applicant tracking system with a public JSON feed. Here is how to read Greenhouse, Lever and Ashby jobs in Python, and a no-code option that also covers Workday and five more systems.

> This example was written with the help of AI. The code was run and checked on 20 November 2026 before publishing.

If you want the open jobs of a list of companies (for a job board, market research, a recruiting tool or your own job search), you do not need to scrape HTML career pages one by one. Most companies host their career page on an applicant tracking system (ATS), and several of them publish the open jobs as public JSON.

This post shows the three easiest ones in Python, the catches you will hit after that, and a no-code option for when you need many companies and many systems.

## How it works
Greenhouse, Lever and Ashby each have a public, read-only endpoint per company. You only need the company's board name, which is usually in its careers URL (`boards.greenhouse.io/stripe`, `jobs.lever.co/palantir`, `jobs.ashbyhq.com/ramp`).

The script is in [`ats_job_listings.py`](ats_job_listings.py).

That is enough for a handful of companies on these three systems. Things to know before you scale it:

- **Full descriptions are optional.** Greenhouse returns them with `?content=true`; Lever includes `descriptionPlain`; Ashby has `descriptionPlain` and, with `?includeCompensation=true`, salary ranges when the company publishes them.
- **Every system has its own shape.** Locations, departments, remote flags, dates and salaries live in different fields, so you will write a normalizer per system.
- **You first have to know which ATS a company uses.** A list of company names does not tell you whether to call Greenhouse or Workday.
- **Workday is the hard one.** Large companies often use Workday, which has no simple per-company feed: each company has its own tenant, data center number and site name, and the job list is a paged POST endpoint.
- **Monitoring needs state.** To get "only jobs that are new since yesterday", you have to remember what you already saw.

## Run it

```bash
python ats_job_listings.py
```

## Hosted version

For many sources, a schedule, "only new items" monitoring or CSV/Excel exports, the same approach runs as the [ATS Jobs Scraper](https://apify.com/webobsidians/ats-jobs-scraper) on Apify. Disclosure: it is built and sold by Web Obsidians, who publish this repository.

## License

MIT
