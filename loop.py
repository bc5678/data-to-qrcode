import os
import data_to_qrcode
import generate_random_file

for i in range(2700, 2600, -1):
	generate_random_file.generate(i)
	print(i)
	try:
		data_to_qrcode.create_qrcode_gif()
		os.system('rm random.txt.backup')
		break
	except:
		os.system('rm random.txt.backup')
		os.system('rm random.txt.backup.jpg')
		continue

print('Success!')
