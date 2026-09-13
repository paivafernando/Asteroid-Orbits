import requests
from datetime import datetime

class Asteroid:

    def find_designations(self, year=None, orbit_class=None):


        base_url = 'https://jsonmock.hackerrank.com/api/asteroids/search'
        response = requests.get(base_url, params={"orbit_class": orbit_class, "page": 1}).json()
        total_pages = response["total_pages"]
                
        data = []

        for page in range(1, total_pages+1):
            resp = requests.get(f"https://jsonmock.hackerrank.com/api/asteroids/search?orbit_class={orbit_class}&page={page}")
            data.extend(resp.json()["data"])
        
        def parse_period(val):
            try:
                return float(val) if val is not None else 1.0
            except (ValueError, TypeError):
                return 1.0

        filtered =  [ 
            {**item, "period_yr": parse_period(item.get("period_yr"))} 
            for item in data 
            if item.get("discovery_date")
            and datetime.strptime(item["discovery_date"], "%Y-%m-%d").year == year
            and orbit_class.lower() == item.get("orbit_class","").lower()

            ]

        designation = [
            x["designation"]
            for x in sorted(filtered, key=lambda x: (x["period_yr"], x["designation"]))
        ]

        return designation       
        