#!/usr/bin/env python
"""Handyman Lead Finder - Main entry point for scraping and exporting leads."""

import os
import csv
import json
import argparse
from datetime import datetime
from pathlib import Path

try:
    from config import *
except ImportError:
    print("ERROR: config.py not found. Make sure you're in the Handyman-Lead-Finder folder.")
    exit(1)

print("\n" + "="*60)
print("HANDYMAN LEAD FINDER - Main Script")
print("="*60)

class LeadFinder:
    """Main class for finding and exporting leads."""
    
    def __init__(self):
        self.leads = []
        self.database_path = DATABASE_PATH
        
    def create_sample_leads(self):
        """Create sample leads for demonstration (real version would scrape)."""
        sample_leads = [
            {
                'name': 'John Smith',
                'phone': '(903) 555-0101',
                'email': 'john.smith@email.com',
                'address': '123 Main St, Tyler, TX 75701',
                'score': 'HOT',
                'reason': 'Posted "need drywall repair ASAP" 2 days ago',
                'source': 'Craigslist',
                'posted_date': '2026-02-15',
                'distance_miles': 35
            },
            {
                'name': 'Sarah Johnson',
                'phone': '(903) 555-0202',
                'email': 'sarah@propertymgmt.com',
                'address': '456 Oak Ave, Longview, TX 75606',
                'score': 'HOT',
                'reason': 'Property manager for 12-unit apartment complex',
                'source': 'Google Maps',
                'posted_date': '2026-02-17',
                'distance_miles': 58
            },
            {
                'name': 'Mike Davis',
                'phone': '(903) 555-0303',
                'email': '',
                'address': '789 Elm St, Beaumont, TX 77701',
                'score': 'WARM',
                'reason': 'Posted "fence repair needed" 10 days ago',
                'source': 'Craigslist',
                'posted_date': '2026-02-07',
                'distance_miles': 92
            },
            {
                'name': 'Property Management LLC',
                'phone': '(903) 555-0404',
                'email': 'info@propmgmt.com',
                'address': '321 Commerce Dr, Texarkana, TX 75501',
                'score': 'HOT',
                'reason': 'Manages 25 rental properties in area',
                'source': 'Google Maps',
                'posted_date': '2026-02-17',
                'distance_miles': 68
            },
            {
                'name': 'Lisa Brown',
                'phone': '(903) 555-0505',
                'email': '',
                'address': '555 Main St, Gladewater, TX 75647',
                'score': 'COLD',
                'reason': 'Vague repair mention, no clear timeline',
                'source': 'Craigslist',
                'posted_date': '2026-01-20',
                'distance_miles': 22
            },
        ]
        return sample_leads
        
    def scrape_leads(self):
        """Scrape leads from configured sources."""
        print("\n[SCRAPING] Finding leads...")
        print(f"   - Center: {CENTER_ZIP} ({CENTER_COORDS[0]}, {CENTER_COORDS[1]})")
        print(f"   - Radius: {RADIUS_MILES} miles")
        print(f"   - Keywords: {', '.join(CRAIGSLIST_SEARCH_KEYWORDS[:5])}...")
        print(f"   - Regions: {', '.join([r.split('/')[-1] for r in CRAIGSLIST_REGIONS])}")
        
        # DEMO: Load sample leads (real version would scrape Craigslist/GoogleMaps)
        print("\n   [NOTE] Using sample leads for demo (real scraper coming soon)")
        self.leads = self.create_sample_leads()
        
        print(f"\n✓ Found {len(self.leads)} leads")
        self.print_summary()
        
    def print_summary(self):
        """Print summary of leads by score."""
        hot = len([l for l in self.leads if l['score'] == 'HOT'])
        warm = len([l for l in self.leads if l['score'] == 'WARM'])
        cold = len([l for l in self.leads if l['score'] == 'COLD'])
        print(f"\n   Breakdown:")
        print(f"   🔥 HOT:   {hot} leads (call immediately)")
        print(f"   🟡 WARM:  {warm} leads (good prospects)")
        print(f"   🔵 COLD:  {cold} leads (follow-up)")
        
    def export_csv(self):
        """Export leads to CSV file."""
        if not self.leads:
            print("No leads to export. Run --scrape first.")
            return
            
        Path(EXPORT_PATH).mkdir(exist_ok=True)
        export_file = os.path.join(EXPORT_PATH, EXPORT_FILENAME)
        
        print(f"\n[EXPORTING] Writing to {export_file}...")
        
        with open(export_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'score', 'name', 'phone', 'email', 'address', 'distance_miles',
                'reason', 'source', 'posted_date'
            ])
            writer.writeheader()
            for lead in self.leads:
                writer.writerow(lead)
        
        print(f"✓ Exported {len(self.leads)} leads to CSV")
        print(f"\n📄 Open in Excel: {export_file}")
        print(f"📊 Or Google Sheets: Upload the CSV file")
        
    def show_stats(self):
        """Show lead statistics."""
        if not self.leads:
            print("No leads found. Run --scrape first.")
            return
            
        print("\n[STATISTICS]")
        print(f"\nTotal Leads: {len(self.leads)}")
        self.print_summary()
        
        print(f"\nAverage Distance: {sum(l['distance_miles'] for l in self.leads) / len(self.leads):.1f} miles")
        print(f"Closest Lead: {min(self.leads, key=lambda x: x['distance_miles'])['distance_miles']} miles")
        print(f"Farthest Lead: {max(self.leads, key=lambda x: x['distance_miles'])['distance_miles']} miles")
        
    def reset(self):
        """Reset database and exported files."""
        print("\n[RESET] Clearing all data...")
        self.leads = []
        print("✓ Database cleared")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Handyman Lead Finder - Find customers needing repairs',
        epilog='Examples:\n  python main.py --scrape\n  python main.py --export leads.csv\n  python main.py --stats'
    )
    parser.add_argument('--scrape', action='store_true', help='Scrape leads from Craigslist and Google Maps')
    parser.add_argument('--export', action='store_true', help='Export leads to CSV')
    parser.add_argument('--stats', action='store_true', help='Show lead statistics')
    parser.add_argument('--reset', action='store_true', help='Reset database')
    
    args = parser.parse_args()
    
    finder = LeadFinder()
    
    if args.scrape:
        finder.scrape_leads()
        finder.export_csv()
    elif args.export:
        finder.export_csv()
    elif args.stats:
        finder.scrape_leads()  # Load demo data
        finder.show_stats()
    elif args.reset:
        finder.reset()
    else:
        print("\nUsage: python main.py [--scrape] [--export] [--stats] [--reset]")
        print("\nRun: python main.py --scrape  to get started")
        print("\nFor help: python main.py --help")
