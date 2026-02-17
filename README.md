# Handyman-Lead-Finder

**Lead generation tool for Deans Handyman Service LLC** targeting a 200-mile radius around Pittsburg, TX (75686). Automatically scrapes Google Maps and Craigslist for handyman and property management leads with intelligent scoring and CSV export.

## Overview

This tool is designed to identify and qualify sales leads for handyman services within the East Texas region. It combines data from multiple sources, scores leads by quality, and provides a clean dashboard for review and outreach.

### Target Area
- **Center**: Pittsburg, TX 75686 (32.97°N, 94.95°W)
- **Radius**: 200 miles
- **Coverage**: Covers most of East/Northeast Texas plus parts of Oklahoma, Arkansas, and Louisiana

## Features

- **Multi-Source Scraping**
  - Google Maps local business finder for property management companies, real estate investors, apartments, RV parks
  - Craigslist classifieds for handyman requests and repair ads
  
- **Lead Scoring System**
  - Hot: Clear need + full contact info (phone + email or website)
  - Warm: Property-related business with partial contact details
  - Cold: Vague needs or missing contact information

- **Lead Management Dashboard**
  - Web-based interface for reviewing leads
  - Mark leads as contacted, booked, or junk
  - Filter by status, score, source, and location

- **Data Export**
  - CSV export for bulk analysis
  - JSON export for API integration
  - Google Sheets sync (optional)

## Project Structure

```
Handyman-Lead-Finder/
├── README.md                      # This file
├── config.py                      # Configuration (radius, keywords, API keys)
├── requirements.txt               # Python dependencies
├── main.py                        # Entry point
├── app.py                         # Flask web app
├── models/
│   ├── lead.py                   # Lead data model
│   └── scoring.py                # Lead scoring logic
├── scrapers/
│   ├── google_maps.py            # Google Maps scraper
│   ├── craigslist.py             # Craigslist scraper
│   └── base_scraper.py           # Base scraper class
├── database/
│   ├── db.py                     # Database initialization
│   └── leads.db                  # SQLite database (generated)
├── templates/
│   ├── base.html                 # Base template
│   ├── leads_table.html          # Leads dashboard
│   └── lead_detail.html          # Individual lead view
├── static/
│   ├── style.css                 # Dashboard styles
│   └── script.js                 # Dashboard interactions
└── exports/
    └── leads_export.csv          # Exported leads (generated)
```

## Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- SQLite (included with Python)

### Installation

```bash
# Clone the repository
git clone https://github.com/Deanthehandyman/Handyman-Lead-Finder.git
cd Handyman-Lead-Finder

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Edit `config.py` with your preferences:

```python
CONFIG = {
    'center_zip': '75686',
    'center_coords': (32.97, -94.95),
    'radius_miles': 200,
    'keywords': [
        'property management',
        'real estate investor',
        'apartment complex',
        'RV park',
        'mobile home park',
        'landlord',
        'handyman',
        'repairs'
    ],
    'database': 'database/leads.db',
    'export_path': 'exports/',
    'flask_port': 5000
}
```

### Run the Tool

```bash
# Start the lead scraper (runs once and saves to database)
python main.py --scrape

# Start the Flask web dashboard
python app.py

# Access at http://localhost:5000
```

## Usage

### Dashboard

Once Flask is running, navigate to `http://localhost:5000` to:

1. **View all leads** in a sortable, filterable table
2. **Filter by**:
   - Status (New, Contacted, Booked, Archived)
   - Score (Hot, Warm, Cold)
   - Source (Google Maps, Craigslist)
   - City or ZIP code

3. **Actions for each lead**:
   - View full details and contact info
   - Mark as "Contacted" or "Booked"
   - Archive or delete
   - Copy phone/email for calling or texting

4. **Export**:
   - Click "Export CSV" to download all leads for bulk outreach
   - Use in Google Sheets, email campaigns, CRM, etc.

### CLI Commands

```bash
# Scrape new leads
python main.py --scrape

# Export to CSV
python main.py --export leads_export.csv

# Show stats
python main.py --stats

# Reset database
python main.py --reset
```

## Lead Sources

### Google Maps
- Searches for local businesses matching keywords
- Extracts: business name, address, phone, website, category
- Automatically deduplicates by phone/website
- Updates contact info if already exists

### Craigslist
- Monitors "household services", "labor", "real estate" sections
- Filters for "handyman", "repair", "install", "remodel" keywords
- Extracts: poster name, phone (if public), email, post URL
- Daily updates (optional automatic refresh)

## Dependencies

See `requirements.txt` for full list. Key packages:
- **Flask**: Web dashboard framework
- **requests**: HTTP requests for scraping
- **BeautifulSoup4**: HTML parsing
- **SQLAlchemy**: Database ORM (optional, can use raw SQL)
- **pandas**: CSV/data export

## Lead Scoring Logic

**HOT (Priority outreach)**
- Property management company OR landlord/investor mentions
- Business has 2+ contact methods (phone + email/website)
- Within 50 miles
- Posted/updated in last 7 days

**WARM (Secondary outreach)**
- Property-related business or AirBnB/rental mentions
- Has at least 1 contact method
- Within 100 miles
- Posted/updated in last 30 days

**COLD (Lower priority)**
- Generic mentions or vague descriptions
- Missing phone or email
- Beyond 100 miles
- Older posts or low relevance score

## Best Practices

1. **Review before calling**: Always check leads in dashboard before mass outreach
2. **Remove duplicates**: The system auto-dedupes, but review for missed duplicates
3. **Personalize outreach**: Use lead details (company name, services needed) in your pitch
4. **Track conversions**: Mark leads as "Booked" to build a conversion rate metric
5. **Update regularly**: Run scraper weekly to catch new leads
6. **A/B test**: Export different lead scores and test which converts best

## Deployment Options

### Option 1: Local/Desktop
- Simple: `python app.py`
- Best for personal use or testing

### Option 2: Cloud (Heroku, AWS, DigitalOcean)
- Deploy Flask app to cloud server
- Access from phone/tablet
- Can schedule automatic daily scrapes with cron/CI

### Option 3: Background Job
- Run scraper on a schedule (e.g., weekly)
- Collect leads in database
- Manual review and export in CSV

## Troubleshooting

**Scraper returns 0 leads**
- Check internet connection
- Verify coordinates are correct in config
- Try increasing radius
- Check if Google/Craigslist URLs are still valid

**Flask dashboard won't start**
- Check if port 5000 is already in use: `lsof -i :5000` (Mac/Linux) or `netstat -ano | findstr :5000` (Windows)
- Change port in config.py or run: `python app.py --port 5001`

**Database errors**
- Delete `database/leads.db` and restart
- Check file permissions in `database/` folder

## Advanced Features (Future)

- [ ] Automated phone/SMS outreach with Twilio
- [ ] Email campaign integration (Mailchimp, ActiveCampaign)
- [ ] CRM sync (HubSpot, Pipedrive)
- [ ] Lead enrichment with Clearbit API
- [ ] Predictive scoring (ML model to predict conversion)
- [ ] Slack notifications for hot leads
- [ ] Mobile app version

## Contributing

Fork, improve, and submit pull requests! Areas for improvement:
- Additional scraper sources (Facebook Marketplace, Indeed)
- Better lead scoring algorithm
- UI/UX improvements
- Performance optimization

## License

MIT License - use freely for your business

## Support

For issues, feature requests, or questions:
1. Check existing GitHub issues
2. Create a new issue with details
3. Include scraper output or error messages if applicable

---

**Made for Deans Handyman Service LLC** | **200-Mile Service Area** | **East Texas Lead Generation**
