# -------------------------------------------------------------
# Paste your data between the triple quotes below
# -------------------------------------------------------------
FLIGHT_CONNECTIONS = """
From	To
New York	London
Tokyo	Sydney
Paris	Berlin
Dubai	Mumbai
San Francisco	Tokyo
Toronto	New York
Shanghai	Singapore
Los Angeles	Mexico City
Istanbul	Athens
Madrid	Rome
Bangkok	Hong Kong
Seoul	Shanghai
Chicago	Toronto
Cape Town	Nairobi
Melbourne	Auckland
Kuala Lumpur	Jakarta
Rio de Janeiro	Buenos Aires
Berlin	Prague
Lima	Bogota
Montreal	Miami
Santiago	Lima
Vancouver	San Francisco
Boston	Dublin
Oslo	Helsinki
Sydney	Brisbane
Singapore	Bangkok
Zurich	Vienna
Tokyo	Seoul
Dubai	Tel Aviv
Doha	Istanbul
Athens	Cairo
Lisbon	Madrid
Warsaw	Budapest
Houston	Phoenix
Dallas	Atlanta
Stockholm	Copenhagen
Hanoi	Ho Chi Minh City
Casablanca	Algiers
Abu Dhabi	Riyadh
Nairobi	Accra
Moscow	Tbilisi
Addis Ababa	Lagos
Tehran	Karachi
Lahore	Islamabad
Dhaka	Colombo
Kathmandu	New Delhi
Ulaanbaatar	Nur-Sultan
Brussels	Amsterdam
Perth	Jakarta
Tashkent	Bishkek
London	Paris
Los Angeles	San Francisco
Hong Kong	Seoul
Chicago	Boston
Rome	Vienna
Miami	Atlanta
Cape Town	Addis Ababa
Jakarta	Singapore
Mexico City	Bogota
Montreal	Toronto
Dubai	Doha
New York	Miami
Tokyo	Osaka
Cairo	Istanbul
Berlin	Warsaw
Rio de Janeiro	Lima
Buenos Aires	Santiago
Melbourne	Sydney
Lisbon	Dublin
Helsinki	Stockholm
Ho Chi Minh City	Bangkok
Casablanca	Nairobi
Vienna	Prague
Dallas	Houston
Phoenix	San Diego
Vancouver	Seattle
Kuala Lumpur	Manila
Manila	Taipei
Taipei	Hong Kong
Nairobi	Accra
Accra	Lagos
Addis Ababa	Luanda
Luanda	Cape Town
Athens	Rome
Oslo	Brussels
Stockholm	Helsinki
Zurich	Amsterdam
Tel Aviv	Istanbul
Tehran	Dubai
Moscow	Helsinki
Doha	Abu Dhabi
Kuwait City	Dubai
Islamabad	New Delhi
Colombo	Mumbai
Karachi	Tehran
Yerevan	Tbilisi
Tbilisi	Baku
Kigali	Nairobi
Muscat	Dubai
Jeddah	Riyadh
Brisbane	Perth
Barcelona	Paris
Caracas	Bogota
Sao Paulo	Buenos Aires
Nairobi	Addis Ababa
Accra	Lagos
Luanda	Kinshasa
Wellington	Auckland
Perth	Wellington
Kigali	Nairobi
Mumbai	New Delhi
Lahore	Karachi
Nur-Sultan	Almaty
Tashkent	Almaty
Ulaanbaatar	Beijing
Beijing	Shanghai
Shanghai	Hong Kong
Hong Kong	Tokyo
Tokyo	Seoul
Seoul	Beijing
Dubai	Singapore
Istanbul	Bangkok
Cairo	Dubai
Istanbul	Casablanca
Mumbai	Singapore
Dubai	Bangkok
"""

CITY_COORDINATES = """
City	Latitude	Longitude
New York	40.7128	-74.006
Los Angeles	34.0522	-118.2437
London	51.5074	-0.1278
Tokyo	35.6895	139.6917
Osaka	34.6937	135.5023
Paris	48.8566	2.3522
New Delhi	28.6139	77.209
Sydney	33.8688	151.2093
Toronto	43.65107	-79.347015
Mexico City	19.432608	-99.133209
Shanghai	31.2304	121.4737
Dubai	25.276987	55.296249
Moscow	55.7558	37.6176
Istanbul	41.0082	28.9784
Mumbai	19.076	72.8777
Bangkok	13.7563	100.5018
Cape Town	33.9249	18.4241
Singapore	1.3521	103.8198
Hong Kong	22.3193	114.1694
Barcelona	41.3851	2.1734
Berlin	52.52	13.405
Rome	41.9028	12.4964
Chicago	41.8781	-87.6298
Buenos Aires	34.6037	-58.3816
Madrid	40.4168	-3.7038
San Francisco	37.7749	-122.4194
Rio de Janeiro	22.9068	-43.1729
Seoul	37.5665	126.978
Santiago	33.4489	-70.6693
Lisbon	38.7223	-9.1393
Vienna	48.2082	16.3738
Amsterdam	52.3676	4.9041
Cairo	30.0444	31.2357
Jakarta	6.2088	106.8456
Lagos	6.5244	3.3792
Kuala Lumpur	3.139	101.6869
Vancouver	49.2827	-123.1207
Manila	14.5995	120.9842
Athens	37.9838	23.7275
Warsaw	52.2297	21.0122
Budapest	47.4979	19.0402
Helsinki	60.1695	24.9354
Stockholm	59.3293	18.0686
Brussels	50.8503	4.3517
Prague	50.0755	14.4378
Oslo	59.9139	10.7522
Zurich	47.3769	8.5417
Tel Aviv	32.0853	34.7818
Doha	25.276987	51.520008
Dublin	53.3498	-6.2603
Lima	12.0464	-77.0428
Bogota	4.711	-74.0721
Montreal	45.5017	-73.5673
Miami	25.7617	-80.1918
Seattle	47.6062	-122.3321
Boston	42.3601	-71.0589
Houston	29.7604	-95.3698
Phoenix	33.4484	-112.074
Dallas	32.7767	-96.797
Atlanta	33.749	-84.388
San Diego	32.7157	-117.1611
Caracas	10.4806	-66.9036
Sao Paulo	23.5505	-46.6333
Melbourne	37.8136	144.9631
Auckland	36.8485	174.7633
Wellington	41.2865	174.7762
Perth	31.9505	115.8605
Brisbane	27.4698	153.0251
Copenhagen	55.6761	12.5683
Hanoi	21.0285	105.8542
Ho Chi Minh City	10.8231	106.6297
Taipei	25.032969	121.565418
Nairobi	1.286389	36.817223
Accra	5.603716	-0.187
Casablanca	33.589886	-7.603869
Algiers	36.737232	3.086472
Kinshasa	4.441931	15.266293
Kigali	1.944072	30.061885
Addis Ababa	9.005401	38.763611
Luanda	8.838333	13.234444
Abu Dhabi	24.453884	54.377343
Muscat	23.588	58.3829
Jeddah	21.2854	39.2376
Riyadh	24.7136	46.6753
Kuwait City	29.3759	47.9774
Tehran	35.6892	51.389
Karachi	24.8607	67.0011
Dhaka	23.8103	90.4125
Lahore	31.5204	74.3587
Colombo	6.9271	79.8612
Kathmandu	27.7172	85.324
Islamabad	33.6844	73.0479
Tashkent	41.2995	69.2401
Baku	40.4093	49.8671
Yerevan	40.1872	44.5152
Tbilisi	41.7151	44.8271
Bishkek	42.8746	74.5698
Nur-Sultan	51.1694	71.4491
Ulaanbaatar	47.8864	106.9057
Almaty	43.2565	76.9283
Beijing	39.9042	116.4074
"""

START_CITY = "Almaty"
END_CITY   = "Auckland"

import math
import heapq
from collections import defaultdict

def haversine(lat1, lon1, lat2, lon2):
    """Haversine distance in km between two (lat,lon) pairs."""
    R = 6371.0
    φ1, φ2 = math.radians(lat1), math.radians(lat2)
    Δφ = math.radians(lat2 - lat1)
    Δλ = math.radians(lon2 - lon1)
    a = math.sin(Δφ/2)**2 + math.cos(φ1)*math.cos(φ2)*math.sin(Δλ/2)**2
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def parse_table(txt, first_line_is_header=True):
    """Return list of lists from tab-separated table string."""
    lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
    return [ln.split('\t') for ln in (lines[1:] if first_line_is_header else lines)]
coords = {}
for city, lat, lon in parse_table(CITY_COORDINATES):
    coords[city] = (float(lat), float(lon))

graph = defaultdict(list)
for frm, to in parse_table(FLIGHT_CONNECTIONS):
    lat1, lon1 = coords[frm]
    lat2, lon2 = coords[to]
    d = haversine(lat1, lon1, lat2, lon2)
    graph[frm].append((to, d))
    graph[to].append((frm, d))  

def shortest_path(graph, start, goal):
    queue = [(0, start, [start])]
    visited = set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        if node == goal:
            return path, cost
        visited.add(node)
        for neighbor, d in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + d, neighbor, path + [neighbor]))
    return None, float('inf')

path, _ = shortest_path(graph, START_CITY, END_CITY)
if path is None:
    print("No route found!")
else:
    print(",".join(path))