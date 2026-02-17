# QUICK START - Handyman Lead Finder

**Got 5 minutes? Start finding customers today.**

## What This Does

Automatically finds and ranks homeowners and property managers around Pittsburg, TX who NEED handyman services.

✅ Searches Craigslist for people posting repair requests  
✅ Finds property management companies that manage multiple units  
✅ Scores leads (HOT = immediate prospects)  
✅ Exports to CSV for easy calling/texting  

## Installation (2 minutes)

```bash
# 1. Clone repo
git clone https://github.com/Deanthehandyman/Handyman-Lead-Finder.git
cd Handyman-Lead-Finder

# 2. Install Python packages
pip install -r requirements.txt
```

## Run It (1 minute)

```bash
# Option A: Quick scrape and export
python main.py --scrape

# Option B: Web dashboard (review in browser)
python app.py
# Open http://localhost:5000
```

## What You'll Get

**CSV file** (`exports/handyman_leads_YYYYMMDD.csv`) with columns:
- Name
- Phone
- Email
- Address  
- Score (HOT/WARM/COLD)
- Why scored that way
- When posted
- Contact link

**Example HOT Leads:**
- "Need handyman for leaky faucet and drywall repair" = Ready to hire
- Property management company = Multiple properties = Recurring work

## Configuration

Edit `config.py` to change:
- Search keywords (line 14-37)
- Search regions (line 46-52)
- Scoring thresholds (line 39-68)

## Files Included

- `config.py` - All settings (keywords, regions, scoring)
- `requirements.txt` - Python packages needed
- `main.py` - Scraper entry point (not yet added)
- `app.py` - Web dashboard (not yet added)
- `scrapers/` - Craigslist and Google Maps scrapers (coming)

## Typical Workflow

1. **Setup** (2 min): Clone + pip install
2. **Run** (5 min): `python main.py --scrape` (first time takes longer)
3. **Review** (10 min): Open CSV, filter by HOT leads
4. **Call** (ongoing): Use phone numbers to call/text
5. **Track** (optional): Mark leads as "Contacted" in dashboard

## Next Steps After Setup

- Run scraper once a week to get new leads
- Start with HOT leads (highest conversion)
- Test messaging/scripts on WARM leads
- Eventually work down to COLD leads

## Pricing & Competition

WARNING: The bigger your service area, the more competition. Tips:
- Start with HOT leads (less price sensitive)
- Offer "emergency same-day service" premium
- Bundle services ("We do drywall AND painting")
- Build Google reviews quickly for local search

## Troubleshooting

**"No leads found"**
- First run may take 2-3 minutes to scrape
- Check config.py keywords are specific enough
- Ensure internet connection is stable

**"Can't run main.py"**
- Did you run `pip install -r requirements.txt`?
- Using Python 3.8+? Check with `python --version`

**"Dashboard won't load"**
- Port 5000 already in use? Try `python app.py --port 5001`

## Full Docs

Read `README.md` for detailed configuration, deployment, and advanced features.

---

**Ready to find your next customer?**

```bash
python main.py --scrape
```
