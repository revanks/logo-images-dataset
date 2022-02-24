import glob

def check_logos():
	with open("logo-list.txt") as list_file:
		logos = list_file.read().splitlines()

	google = list(map(lambda x: x.split("\\")[-1], glob.glob("google/*")))
	bing = list(map(lambda x: x.split("\\")[-1], glob.glob("bing/*")))
	duckduckgo = list(map(lambda x: x.split("\\")[-1], glob.glob("duckduckgo/*")))
	yahoo = list(map(lambda x: x.split("\\")[-1], glob.glob("yahoo/*")))
	logodix = list(map(lambda x: x.split("\\")[-1], glob.glob("logodix/*")))


	for logo in logos:
		if logo not in google:
			print(logo)
		if logo not in bing:
			print(logo)
		if logo not in duckduckgo:
			print(logo)
		if logo not in yahoo:
			print(logo)
		if logo not in logodix:
			print(logo)

if __name__ == '__main__':
	check_logos()