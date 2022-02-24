import glob
import os

def count_images():
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


if __name__ == "__main__":
	count_images()
