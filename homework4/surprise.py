# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def name_star(dict_name): 
	for target_name in dict_name: 
		print (target_name)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def spectral_type (dict_name): 
	for target_name, info in dict_name.items(): 
		print (f"{target_name} : {info["Spectral Type"]}")
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def magnitudes_greater_than(dict_name, threshold=0.1):
	for target_name, info in dict_name.items(): 
		if info["Magnitude"] > threshold: 
			print (f"{target_name} (mag = {info["Magnitude"]})")

# 4) Look up another target, add all the necessary information to the targets list.
targets ["arcturus"] = {
	"RA": "14h 15m 39.7s", 
	"Dec": "+19° 10' 56''", 
	"Magnitude": -0.05, 
	"Spectral Type": "K1.5III"
}
 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def brightest_closest_20(targets): 
	best_star = None
	best_diff = None 
	for star, info in targets.items(): 
		dec_deg = int(info["Dec"].split("°")[0].replace("−", "-"))
		diff = abs(dec_deg - 20)
		if best_star is None or diff < best_diff: 
			best_star = star 
			best_diff = diff 
		elif diff == best_diff: 
			if info["Magnitude"] < targets[best_star]["Magnitude"]:
				best_star = star 
	return best_star

# 6) What is your favorite constellation?
#the cal star I got to see it in ASTRO C10 

print(name_star(targets))
print(spectral_type(targets))
print (magnitudes_greater_than(targets))
print(brightest_closest_20(targets))