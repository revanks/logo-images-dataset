import glob
import os

# Count
print("# Number of images\n")

c_google = len(glob.glob("google/*/*"))
c_bing = len(glob.glob("bing/*/*"))
c_duckduckgo = len(glob.glob("duckduckgo/*/*"))
c_yahoo = len(glob.glob("yahoo/*/*"))
c_logodix = len(glob.glob("logodix/*/*"))

print(f"Google: {c_google}")
print(f"Bing: {c_bing}")
print(f"DuckDuckGo: {c_duckduckgo}")
print(f"Yahoo: {c_yahoo}")
print(f"Logodix: {c_logodix}")

print("\nTotal: ", end="")
print(c_google + c_bing + c_duckduckgo + c_yahoo + c_logodix)


# Check for empty directories
print("\n# Empty directories")
for search_engine in ["google", "bing", "duckduckgo", "yahoo", "logodix"]:
	for each in glob.glob(f"{search_engine}/*"):
		if(len(os.listdir(each))) == 0:
			print(each)

# Check logo
print("\n# Check logos")
logos = {}

for search_engine in ["google", "bing", "duckduckgo", "yahoo", "logodix"]:
	logos[search_engine] = []
	for each in glob.glob(f"{search_engine}/*"):
		logos[search_engine].append(each.split('\\')[-1])

print(set(logos['google']) - set(logos['logodix']))
print(set(logos['logodix']) - set(logos['google']))


