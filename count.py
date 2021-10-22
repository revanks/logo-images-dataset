import glob

count = 0
for each in range(65, 91):
	subfolder_list = glob.glob(f"{chr(each)}/*")
	count += len(subfolder_list)
	print(chr(each), len(subfolder_list))

print(count)
