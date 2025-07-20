import re
from shapely.geometry import Point, Polygon

# --- Paste franchisee + city table here ---
raw_table = """
Franchisee	Cities [Latitude, Longitude]
1	
New Delhi [28.6139,77.209]
Mumbai [19.076,72.8777]
Muscat [23.588,58.3829]
Karachi [24.8607,67.0011]
Lahore [31.5204,74.3587]
Colombo [6.9271,79.8612]
Kathmandu [27.7172,85.324]
2	
Jakarta [6.2088,106.8456]
Manila [14.5995,120.9842]
Ho Chi Minh City [10.8231,106.6297]
Hanoi [21.0285,105.8542]
Singapore [1.3521,103.8198]
Hong Kong [22.3193,114.1694]
3	
Warsaw [52.2297,21.0122]
Helsinki [60.1695,24.9354]
Stockholm [59.3293,18.0686]
Moscow [55.7558,37.6176]
Istanbul [41.0082,28.9784]
4	
Copenhagen [55.6761,12.5683]
Berlin [52.52,13.405]
Helsinki [60.1695,24.9354]
Stockholm [59.3293,18.0686]
Oslo [59.9139,10.7522]
Amsterdam [52.3676,4.9041]
5	
Nur-Sultan [51.1694,71.4491]
Istanbul [41.0082,28.9784]
Moscow [55.7558,37.6176]
Baku [40.4093,49.8671]
Yerevan [40.1872,44.5152]
Tbilisi [41.7151,44.8271]
6	
Cairo [30.0444,31.2357]
Athens [37.9838,23.7275]
Warsaw [52.2297,21.0122]
Budapest [47.4979,19.0402]
Istanbul [41.0082,28.9784]
Rome [41.9028,12.4964]
7	
London [51.5074,-0.1278]
Paris [48.8566,2.3522]
Brussels [50.8503,4.3517]
Prague [50.0755,14.4378]
Zurich [47.3769,8.5417]
Berlin [52.52,13.405]
Amsterdam [52.3676,4.9041]
8	
Nur-Sultan [51.1694,71.4491]
Ulaanbaatar [47.8864,106.9057]
Helsinki [60.1695,24.9354]
Moscow [55.7558,37.6176]
9	
New York [40.7128,-74.006]
Toronto [43.65107,-79.347015]
Atlanta [33.749,-84.388]
Santiago [33.4489,-70.6693]
10	
Abu Dhabi [24.453884,54.377343]
Jeddah [21.2854,39.2376]
Riyadh [24.7136,46.6753]
Kigali [1.944072,30.061885]
Addis Ababa [9.005401,38.763611]
Tel Aviv [32.0853,34.7818]
11	
Barcelona [41.3851,2.1734]
Rome [41.9028,12.4964]
Madrid [40.4168,-3.7038]
Casablanca [33.589886,-7.603869]
Algiers [36.737232,3.086472]
12	
Tel Aviv [32.0853,34.7818]
Kuwait City [29.3759,47.9774]
Tehran [35.6892,51.389]
Karachi [24.8607,67.0011]
Tashkent [41.2995,69.2401]
Baku [40.4093,49.8671]
Yerevan [40.1872,44.5152]
13	
Miami [25.7617,-80.1918]
Houston [29.7604,-95.3698]
Dallas [32.7767,-96.797]
Atlanta [33.749,-84.388]
14	
Dubai [25.276987,55.296249]
Abu Dhabi [24.453884,54.377343]
Doha [25.276987,51.520008]
Kuwait City [29.3759,47.9774]
Tehran [35.6892,51.389]
Karachi [24.8607,67.0011]
15	
Cairo [30.0444,31.2357]
Jeddah [21.2854,39.2376]
Istanbul [41.0082,28.9784]
Luanda [8.838333,13.234444]
Tel Aviv [32.0853,34.7818]
16	
London [51.5074,-0.1278]
Paris [48.8566,2.3522]
Casablanca [33.589886,-7.603869]
Dublin [53.3498,-6.2603]
Buenos Aires [34.6037,-58.3816]
Madrid [40.4168,-3.7038]
Lisbon [38.7223,-9.1393]
17	
Lagos [6.5244,3.3792]
Accra [5.603716,-0.187]
Casablanca [33.589886,-7.603869]
Algiers [36.737232,3.086472]
Kinshasa [4.441931,15.266293]
18	
Bishkek [42.8746,74.5698]
Nur-Sultan [51.1694,71.4491]
Karachi [24.8607,67.0011]
Islamabad [33.6844,73.0479]
Tashkent [41.2995,69.2401]
Baku [40.4093,49.8671]
19	
Cairo [30.0444,31.2357]
Cape Town [33.9249,18.4241]
Rome [41.9028,12.4964]
Athens [37.9838,23.7275]
Algiers [36.737232,3.086472]
20	
Lima [12.0464,-77.0428]
Miami [25.7617,-80.1918]
Houston [29.7604,-95.3698]
Mexico City [19.432608,-99.133209]
21	
Perth [31.9505,115.8605]
Osaka [34.6937,135.5023]
Manila [14.5995,120.9842]
Beijing [39.9042,116.4074]
Taipei [25.032969,121.565418]
Shanghai [31.2304,121.4737]
Hong Kong [22.3193,114.1694]
22	
Miami [25.7617,-80.1918]
Buenos Aires [34.6037,-58.3816]
Atlanta [33.749,-84.388]
Santiago [33.4489,-70.6693]
Caracas [10.4806,-66.9036]
23	
Los Angeles [34.0522,-118.2437]
Seattle [47.6062,-122.3321]
Chicago [41.8781,-87.6298]
Phoenix [33.4484,-112.074]
San Diego [32.7157,-117.1611]
Mexico City [19.432608,-99.133209]
24	
Singapore [1.3521,103.8198]
Muscat [23.588,58.3829]
Kuala Lumpur [3.139,101.6869]
Nairobi [1.286389,36.817223]
Colombo [6.9271,79.8612]
Addis Ababa [9.005401,38.763611]
25	
Ulaanbaatar [47.8864,106.9057]
Almaty [43.2565,76.9283]
Hanoi [21.0285,105.8542]
Dhaka [23.8103,90.4125]
Kathmandu [27.7172,85.324]
26	
Lisbon [38.7223,-9.1393]
Buenos Aires [34.6037,-58.3816]
Rio de Janeiro [22.9068,-43.1729]
Caracas [10.4806,-66.9036]
Sao Paulo [23.5505,-46.6333]
27	
Accra [5.603716,-0.187]
Mexico City [19.432608,-99.133209]
Kigali [1.944072,30.061885]
Lima [12.0464,-77.0428]
Bogota [4.711,-74.0721]
Rio de Janeiro [22.9068,-43.1729]
Caracas [10.4806,-66.9036]
28	
Accra [5.603716,-0.187]
Kinshasa [4.441931,15.266293]
Kigali [1.944072,30.061885]
Luanda [8.838333,13.234444]
29	
Vancouver [49.2827,-123.1207]
Seattle [47.6062,-122.3321]
Chicago [41.8781,-87.6298]
San Francisco [37.7749,-122.4194]
30	
Lima [12.0464,-77.0428]
Caracas [10.4806,-66.9036]
Miami [25.7617,-80.1918]
31	
Jakarta [6.2088,106.8456]
Singapore [1.3521,103.8198]
Kuala Lumpur [3.139,101.6869]
Ho Chi Minh City [10.8231,106.6297]
32	
Auckland [36.8485,174.7633]
Wellington [41.2865,174.7762]
Brisbane [27.4698,153.0251]
Sydney [33.8688,151.2093]
33	
Vancouver [49.2827,-123.1207]
Montreal [45.5017,-73.5673]
Chicago [41.8781,-87.6298]
Toronto [43.65107,-79.347015]
Atlanta [33.749,-84.388]
34	
Kuala Lumpur [3.139,101.6869]
Ho Chi Minh City [10.8231,106.6297]
Colombo [6.9271,79.8612]
Bangkok [13.7563,100.5018]
35	
Ulaanbaatar [47.8864,106.9057]
Perth [31.9505,115.8605]
Beijing [39.9042,116.4074]
Hanoi [21.0285,105.8542]
Shanghai [31.2304,121.4737]
Hong Kong [22.3193,114.1694]
Seoul [37.5665,126.978]
36	
Warsaw [52.2297,21.0122]
Budapest [47.4979,19.0402]
Prague [50.0755,14.4378]
Berlin [52.52,13.405]
Rome [41.9028,12.4964]
Vienna [48.2082,16.3738]
37	
Paris [48.8566,2.3522]
Prague [50.0755,14.4378]
Zurich [47.3769,8.5417]
Barcelona [41.3851,2.1734]
Rome [41.9028,12.4964]
Madrid [40.4168,-3.7038]
Vienna [48.2082,16.3738]
38	
Abu Dhabi [24.453884,54.377343]
Muscat [23.588,58.3829]
Karachi [24.8607,67.0011]
Dubai [25.276987,55.296249]
Addis Ababa [9.005401,38.763611]
39	
Dublin [53.3498,-6.2603]
London [51.5074,-0.1278]
Montreal [45.5017,-73.5673]
Oslo [59.9139,10.7522]
Amsterdam [52.3676,4.9041]
40	
Bogota [4.711,-74.0721]
Nairobi [1.286389,36.817223]
Kigali [1.944072,30.061885]
Addis Ababa [9.005401,38.763611]
41	
Tokyo [35.6895,139.6917]
Osaka [34.6937,135.5023]
Sydney [33.8688,151.2093]
Shanghai [31.2304,121.4737]
Seoul [37.5665,126.978]
Melbourne [37.8136,144.9631]
42	
Wellington [41.2865,174.7762]
Ulaanbaatar [47.8864,106.9057]
Sydney [33.8688,151.2093]
Helsinki [60.1695,24.9354]
Seoul [37.5665,126.978]
Melbourne [37.8136,144.9631]
43	
Doha [25.276987,51.520008]
Abu Dhabi [24.453884,54.377343]
Riyadh [24.7136,46.6753]
Kuwait City [29.3759,47.9774]
Tel Aviv [32.0853,34.7818]
44	
Stockholm [59.3293,18.0686]
Berlin [52.52,13.405]
Warsaw [52.2297,21.0122]
45	
Copenhagen [55.6761,12.5683]
Oslo [59.9139,10.7522]
Amsterdam [52.3676,4.9041]
46	
Cairo [30.0444,31.2357]
Lagos [6.5244,3.3792]
Algiers [36.737232,3.086472]
Kinshasa [4.441931,15.266293]
Luanda [8.838333,13.234444]
Cape Town [33.9249,18.4241]
47	
Mexico City [19.432608,-99.133209]
Chicago [41.8781,-87.6298]
Houston [29.7604,-95.3698]
Phoenix [33.4484,-112.074]
Dallas [32.7767,-96.797]
Atlanta [33.749,-84.388]
48	
Bishkek [42.8746,74.5698]
Nur-Sultan [51.1694,71.4491]
Ulaanbaatar [47.8864,106.9057]
Almaty [43.2565,76.9283]
Karachi [24.8607,67.0011]
Lahore [31.5204,74.3587]
Islamabad [33.6844,73.0479]
49	
Hanoi [21.0285,105.8542]
Ho Chi Minh City [10.8231,106.6297]
Dhaka [23.8103,90.4125]
Colombo [6.9271,79.8612]
Bangkok [13.7563,100.5018]
50	
Jeddah [21.2854,39.2376]
Kigali [1.944072,30.061885]
Luanda [8.838333,13.234444]
51	
Montreal [45.5017,-73.5673]
Oslo [59.9139,10.7522]
Vancouver [49.2827,-123.1207]
52	
New York [40.7128,-74.006]
Dublin [53.3498,-6.2603]
Montreal [45.5017,-73.5673]
Buenos Aires [34.6037,-58.3816]
Boston [42.3601,-71.0589]
Santiago [33.4489,-70.6693]
53	
Dhaka [23.8103,90.4125]
Colombo [6.9271,79.8612]
Kathmandu [27.7172,85.324]
Mumbai [19.076,72.8777]
54	
Auckland [36.8485,174.7633]
Brisbane [27.4698,153.0251]
Tokyo [35.6895,139.6917]
Manila [14.5995,120.9842]
Osaka [34.6937,135.5023]
Sydney [33.8688,151.2093]
Singapore [1.3521,103.8198]
55	
Tel Aviv [32.0853,34.7818]
Istanbul [41.0082,28.9784]
Yerevan [40.1872,44.5152]
Tbilisi [41.7151,44.8271]
56	
Los Angeles [34.0522,-118.2437]
Seattle [47.6062,-122.3321]
San Francisco [37.7749,-122.4194]
San Diego [32.7157,-117.1611]
57	
Caracas [10.4806,-66.9036]
Sao Paulo [23.5505,-46.6333]
Buenos Aires [34.6037,-58.3816]
58	
Shanghai [31.2304,121.4737]
Osaka [34.6937,135.5023]
Taipei [25.032969,121.565418]
59	
New York [40.7128,-74.006]
Toronto [43.65107,-79.347015]
Montreal [45.5017,-73.5673]
60	
Almaty [43.2565,76.9283]
New Delhi [28.6139,77.209]
Lahore [31.5204,74.3587]
Kathmandu [27.7172,85.324]
61	
London [51.5074,-0.1278]
Brussels [50.8503,4.3517]
Amsterdam [52.3676,4.9041]
62	
Rio de Janeiro [22.9068,-43.1729]
Accra [5.603716,-0.187]
Casablanca [33.589886,-7.603869]
Lisbon [38.7223,-9.1393]
"""

# --- Paste pickup points here ---
raw_pickups = """
51.5689	-4.9461
38.9055	-103.5088
39.9186	165.4217
47.7196	-85.2553
36.9017	132.8251
"""

franchise_data = {}
current_fid = None

for line in raw_table.strip().splitlines():
    line = line.strip()
    if not line or line.startswith("Franchisee"):
        continue
    if re.fullmatch(r"\d+", line):
        current_fid = int(line)
        franchise_data[current_fid] = {}
    else:
        match = re.match(r"^(.*?)\s*\[\s*([0-9\.\-]+)\s*,\s*([0-9\.\-]+)\s*\]$", line)
        if match and current_fid:
            city = match.group(1).strip()
            lat = float(match.group(2))
            lon = float(match.group(3))
            franchise_data[current_fid][city] = [lat, lon]
pickup_points = []
pickup_lines = raw_pickups.strip().splitlines()

for line in pickup_lines:
    line = line.strip()
    if not line:
        continue
    parts = re.split(r"[\s,]+", line)
    if len(parts) >= 2:
        lat = float(parts[0])
        lon = float(parts[1])
        pickup_points.append((lat, lon))

cities = {}
regions = []

for fid, city_dict in franchise_data.items():
    region_city_names = []
    for city, coords in city_dict.items():
        cities[city] = coords
        region_city_names.append(city)
    regions.append(region_city_names)

franchise_polygons = []
for i, region_city_names in enumerate(regions, start=1):
    try:
        coords = [(cities[city][1], cities[city][0]) for city in region_city_names]
        polygon = Polygon(coords)
        if not polygon.is_valid:
            polygon = polygon.convex_hull
        franchise_polygons.append((i, polygon))
    except KeyError as e:
        print(f"City '{e.args[0]}' not found in city list.")

results = []
for lat, lon in pickup_points:
    point = Point(lon, lat)
    assigned = None
    for fid, polygon in franchise_polygons:
        if polygon.contains(point):
            assigned = fid
            break
    results.append(str(assigned) if assigned else "Unassigned")

print("Franchisees:", ",".join(results))
