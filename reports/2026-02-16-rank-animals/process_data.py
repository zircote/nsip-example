#!/usr/bin/env python3
"""
Process NSIP data for rank animals flock action.
"""

import json
import csv
from datetime import datetime

# Animal data from NSIP MCP tools
animals_data = [
    {"lpn_id":"6401492020FLE249","breed":"Katahdin","date_of_birth":"2/5/2020","gender":"Female","status":"CURRENT","sire":"6401492019FLE124","dam":"6401492018FLE035","registration_number":"","total_progeny":6,"flock_count":1,"genotyped":"No","traits":{"YWT":{"name":"YWT","value":3.625,"accuracy":63},"PWWT":{"name":"PWWT","value":4.659,"accuracy":73},"WWT":{"name":"WWT","value":3.051,"accuracy":71},"BWT":{"name":"BWT","value":0.244,"accuracy":74},"NLB":{"name":"NLB","value":0.118,"accuracy":58}},"contact_info":{"farm_name":"Beyond Blessed Farm","contact_name":"Chris and Mandy Fletcher","phone":"(276)-759-4718","email":"mbfletcher08@gmail.com","city":"Abingdon","state":"VA"}},
    {"lpn_id":"6401492022FLE002","breed":"Katahdin","date_of_birth":"1/23/2022","gender":"Female","status":"CURRENT","sire":"6401492020FLE120","dam":"6401492020FLE230","registration_number":"","total_progeny":5,"flock_count":1,"genotyped":"50K Genotyped","traits":{"WWT":{"name":"WWT","value":-0.014,"accuracy":64},"PWWT":{"name":"PWWT","value":-0.9,"accuracy":66},"NLB":{"name":"NLB","value":0.06,"accuracy":50},"YWT":{"name":"YWT","value":-1.324,"accuracy":55},"BWT":{"name":"BWT","value":-0.176,"accuracy":66}},"contact_info":{"farm_name":"Beyond Blessed Farm","contact_name":"Chris and Mandy Fletcher","phone":"(276)-759-4718","email":"mbfletcher08@gmail.com","city":"Abingdon","state":"VA"}},
    {"lpn_id":"6401492023FLE078","breed":"Katahdin","date_of_birth":"2/21/2023","gender":"Female","status":"CURRENT","sire":"6401492018DRW522","dam":"6401492021FLE144","registration_number":"","total_progeny":0,"flock_count":0,"genotyped":"No","traits":{"YWT":{"name":"YWT","value":0.677,"accuracy":52},"NLB":{"name":"NLB","value":-0.052,"accuracy":50},"BWT":{"name":"BWT","value":0.306,"accuracy":64},"WWT":{"name":"WWT","value":1.62,"accuracy":62},"PWWT":{"name":"PWWT","value":1.615,"accuracy":61}},"contact_info":{"farm_name":"Beyond Blessed Farm","contact_name":"Chris and Mandy Fletcher","phone":"(276)-759-4718","email":"mbfletcher08@gmail.com","city":"Abingdon","state":"VA"}},
    {"lpn_id":"6401492025FLE011","breed":"Katahdin","date_of_birth":"2/17/2025","gender":"Female","status":"CURRENT","sire":"6402382024NCS310","dam":"6401492016166045","registration_number":"","total_progeny":0,"flock_count":0,"genotyped":"No","traits":{"BWT":{"name":"BWT","value":0.001,"accuracy":61},"PWWT":{"name":"PWWT","value":3.46,"accuracy":61},"YWT":{"name":"YWT","value":2.191,"accuracy":52},"NLB":{"name":"NLB","value":0.175,"accuracy":45},"WWT":{"name":"WWT","value":2.193,"accuracy":59}},"contact_info":{"farm_name":"Beyond Blessed Farm","contact_name":"Chris and Mandy Fletcher","phone":"(276)-759-4718","email":"mbfletcher08@gmail.com","city":"Abingdon","state":"VA"}},
    {"lpn_id":"6401492025FLE024","breed":"Katahdin","date_of_birth":"2/20/2025","gender":"Female","status":"CURRENT","sire":"6401492024FLE176","dam":"6401492023FLE010","registration_number":"","total_progeny":0,"flock_count":0,"genotyped":"No","traits":{"WWT":{"name":"WWT","value":2.842,"accuracy":58},"YWT":{"name":"YWT","value":4.615,"accuracy":49},"PWWT":{"name":"PWWT","value":4.99,"accuracy":60},"BWT":{"name":"BWT","value":0.473,"accuracy":60},"NLB":{"name":"NLB","value":0.126,"accuracy":36}},"contact_info":{"farm_name":"Beyond Blessed Farm","contact_name":"Chris and Mandy Fletcher","phone":"(276)-759-4718","email":"mbfletcher08@gmail.com","city":"Abingdon","state":"VA"}},
    {"lpn_id":"6401492025FLE029","breed":"Katahdin","date_of_birth":"2/21/2025","gender":"Female","status":"CURRENT","sire":"6402382024NCS310","dam":"6401492024FLE048","registration_number":"","total_progeny":0,"flock_count":0,"genotyped":"No","traits":{"NLB":{"name":"NLB","value":0.112,"accuracy":41},"PWWT":{"name":"PWWT","value":3.976,"accuracy":59},"YWT":{"name":"YWT","value":3.581,"accuracy":49},"WWT":{"name":"WWT","value":2.129,"accuracy":56},"BWT":{"name":"BWT","value":0.177,"accuracy":58}},"contact_info":{"farm_name":"Beyond Blessed Farm","contact_name":"Chris and Mandy Fletcher","phone":"(276)-759-4718","email":"mbfletcher08@gmail.com","city":"Abingdon","state":"VA"}},
    {"lpn_id":"6401492025FLE047","breed":"Katahdin","date_of_birth":"2/24/2025","gender":"Female","status":"CURRENT","sire":"6401492024FLE176","dam":"6401492023FLE087","registration_number":"","total_progeny":0,"flock_count":0,"genotyped":"No","traits":{"YWT":{"name":"YWT","value":5.056,"accuracy":49},"BWT":{"name":"BWT","value":0.432,"accuracy":59},"PWWT":{"name":"PWWT","value":5.094,"accuracy":60},"NLB":{"name":"NLB","value":0.042,"accuracy":36},"WWT":{"name":"WWT","value":2.951,"accuracy":57}},"contact_info":{"farm_name":"Beyond Blessed Farm","contact_name":"Chris and Mandy Fletcher","phone":"(276)-759-4718","email":"mbfletcher08@gmail.com","city":"Abingdon","state":"VA"}},
    {"lpn_id":"6401492025FLE082","breed":"Katahdin","date_of_birth":"2/28/2025","gender":"Female","status":"CURRENT","sire":"6401492022FLE382","dam":"6401492019FLE061","registration_number":"","total_progeny":0,"flock_count":0,"genotyped":"No","traits":{"BWT":{"name":"BWT","value":0.334,"accuracy":65},"PWWT":{"name":"PWWT","value":4.796,"accuracy":65},"YWT":{"name":"YWT","value":4.41,"accuracy":55},"WWT":{"name":"WWT","value":2.702,"accuracy":63},"NLB":{"name":"NLB","value":0.113,"accuracy":45}},"contact_info":{"farm_name":"Beyond Blessed Farm","contact_name":"Chris and Mandy Fletcher","phone":"(276)-759-4718","email":"mbfletcher08@gmail.com","city":"Abingdon","state":"VA"}},
    {"lpn_id":"6401492025FLE087","breed":"Katahdin","date_of_birth":"3/2/2025","gender":"Female","status":"CURRENT","sire":"6401492022FLE382","dam":"6401492022FLE013","registration_number":"","total_progeny":0,"flock_count":0,"genotyped":"No","traits":{"NLB":{"name":"NLB","value":0.133,"accuracy":44},"YWT":{"name":"YWT","value":5.728,"accuracy":53},"BWT":{"name":"BWT","value":0.354,"accuracy":63},"WWT":{"name":"WWT","value":3.072,"accuracy":61},"PWWT":{"name":"PWWT","value":5.888,"accuracy":64}},"contact_info":{"farm_name":"Beyond Blessed Farm","contact_name":"Chris and Mandy Fletcher","phone":"(276)-759-4718","email":"mbfletcher08@gmail.com","city":"Abingdon","state":"VA"}},
    {"lpn_id":"6401492025FLE008","breed":"Katahdin","date_of_birth":"2/16/2025","gender":"Female","status":"CURRENT","sire":"6402382024NCS310","dam":"6401492022FLE040","registration_number":"","total_progeny":0,"flock_count":0,"genotyped":"No","traits":{"BWT":{"name":"BWT","value":0.169,"accuracy":62},"WWT":{"name":"WWT","value":2.726,"accuracy":61},"YWT":{"name":"YWT","value":3.593,"accuracy":53},"PWWT":{"name":"PWWT","value":4.49,"accuracy":63},"NLB":{"name":"NLB","value":0.164,"accuracy":44}},"contact_info":{"farm_name":"Beyond Blessed Farm","contact_name":"Chris and Mandy Fletcher","phone":"(276)-759-4718","email":"mbfletcher08@gmail.com","city":"Abingdon","state":"VA"}},
    {"lpn_id":"6402382024NCS310","breed":"Katahdin","date_of_birth":"2/13/2024","gender":"Male","status":"CURRENT","sire":"6400462020VPI007","dam":"6402382022NCS087","registration_number":"","total_progeny":25,"flock_count":1,"genotyped":"50K Genotyped","traits":{"BWT":{"name":"BWT","value":-0.235,"accuracy":80},"WWT":{"name":"WWT","value":1.214,"accuracy":78},"YWT":{"name":"YWT","value":0.796,"accuracy":68},"PWWT":{"name":"PWWT","value":1.764,"accuracy":81},"NLB":{"name":"NLB","value":0.092,"accuracy":55}},"contact_info":{"farm_name":"North Carolina State University Katahdins","contact_name":"Andrew Weaver","phone":"(989)-708-2557","email":"arweave3@ncsu.edu","city":"Raleigh","state":"NC"}},
    {"lpn_id":"6401492025FLE141","breed":"Katahdin","date_of_birth":"2/24/2025","gender":"Male","status":"CURRENT","sire":"6401552024GBR123","dam":"6401492020FLE205","registration_number":"","total_progeny":0,"flock_count":0,"genotyped":"No","traits":{"BWT":{"name":"BWT","value":0.264,"accuracy":61},"WWT":{"name":"WWT","value":1.269,"accuracy":59},"YWT":{"name":"YWT","value":2.208,"accuracy":47},"PWWT":{"name":"PWWT","value":2.49,"accuracy":58},"NLB":{"name":"NLB","value":-0.016,"accuracy":38}},"contact_info":{"farm_name":"Beyond Blessed Farm","contact_name":"Chris and Mandy Fletcher","phone":"(276)-759-4718","email":"mbfletcher08@gmail.com","city":"Abingdon","state":"VA"}},
]

# Breed trait ranges for Katahdin (breed_id: 640)
trait_ranges = {
    "BWT": {"min": -0.939, "max": 1.299},
    "WWT": {"min": -3.02, "max": 6.183},
    "YWT": {"min": -9.528, "max": 10.362},
    "PWWT": {"min": -7.102, "max": 9.401},
    "NLB": {"min": -0.361, "max": 0.693}
}

# Default weights for hair sheep
weights = {
    "BWT": -1.0,
    "WWT": 2.0,
    "YWT": 1.5,
    "PWWT": 1.0,
    "NLB": 1.0
}

def calculate_score(animal):
    """Calculate weighted score for an animal."""
    score = 0.0
    contributions = {}
    
    for trait_name, weight in weights.items():
        if trait_name in animal["traits"]:
            trait = animal["traits"][trait_name]
            value = trait["value"]
            accuracy = trait["accuracy"]
            contribution = value * weight * (accuracy / 100.0)
            score += contribution
            contributions[trait_name] = contribution
    
    return score, contributions

def calculate_percentile(value, min_val, max_val):
    """Calculate percentile position within breed range."""
    if max_val == min_val:
        return 50
    percentile = ((value - min_val) / (max_val - min_val)) * 100
    return max(0, min(100, percentile))

# Calculate scores for all animals
results = []
for animal in animals_data:
    score, contributions = calculate_score(animal)
    results.append({
        "animal": animal,
        "score": score,
        "contributions": contributions
    })

# Sort by WWT value (as specified in sort_trait)
results.sort(key=lambda x: x["animal"]["traits"]["WWT"]["value"], reverse=True)

# Add ranks
for i, result in enumerate(results, 1):
    result["rank"] = i

# Write CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    # Header
    writer.writerow([
        "rank", "lpn_id", "gender", "dob", "score",
        "BWT_value", "BWT_accuracy", "BWT_contribution",
        "WWT_value", "WWT_accuracy", "WWT_contribution",
        "YWT_value", "YWT_accuracy", "YWT_contribution",
        "PWWT_value", "PWWT_accuracy", "PWWT_contribution",
        "NLB_value", "NLB_accuracy", "NLB_contribution"
    ])
    
    # Data rows
    for result in results:
        animal = result["animal"]
        traits = animal["traits"]
        contributions = result["contributions"]
        
        row = [
            result["rank"],
            animal["lpn_id"],
            animal["gender"],
            animal["date_of_birth"],
            f"{result['score']:.2f}",
        ]
        
        for trait_name in ["BWT", "WWT", "YWT", "PWWT", "NLB"]:
            if trait_name in traits:
                row.extend([
                    f"{traits[trait_name]['value']:.3f}",
                    traits[trait_name]["accuracy"],
                    f"{contributions[trait_name]:.3f}"
                ])
            else:
                row.extend(["", "", ""])
        
        writer.writerow(row)

print(f"Processed {len(results)} animals")
print(f"CSV written to data.csv")
print(f"\nTop 3 by WWT:")
for i, result in enumerate(results[:3], 1):
    animal = result["animal"]
    ww = animal["traits"]["WWT"]
    print(f"{i}. {animal['lpn_id']}: WWT = +{ww['value']:.2f} ({ww['accuracy']}%)")
