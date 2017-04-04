import os
import sys
import qrcode
import subprocess
import imageio

file_name = sys.argv[1]
qrcode_file_size = 2500

def generate_qrcode(src_file, file_type):
	if (file_type == 'text'):
		f = open(src_file, 'r')
	elif (file_type == 'binary'):
		f = open(src_file, 'rb')
	qr = qrcode.QRCode(version = 40, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 3, border = 4)
	qr.add_data(f.read())
	qr.make()
	f.close()
	img = qr.make_image()
	img.save(src_file + '.png') 


result = subprocess.run(['file', file_name], stdout=subprocess.PIPE).stdout.decode('utf-8')
print(result)

if ('text' not in result):
#	cmd = 'od -A n -t x1 ' + filename + ' | tr -d " \n" > ' + filename + '.txt'
#	os.system(cmd)
#	print(cmd)
#	filename = filename + '.txt'
	file_type = 'binary'
else:
	file_type = 'text'

if (os.stat(file_name).st_size > qrcode_file_size):
	cmd = 'split -b ' + str(qrcode_file_size) + ' ' + file_name + ' ' + file_name + '.'
	print(cmd)
	os.system(cmd)
else:
	cmd = 'cp ' + file_name + ' ' + file_name + '.backup'
	print(cmd)
	os.system(cmd)

result = subprocess.run(['ls'], stdout=subprocess.PIPE).stdout.decode('utf-8')

kargs = { 'duration': 0.3 }
with imageio.get_writer('movie.gif', mode='I', **kargs) as writer:
	image = imageio.imread('white.jpg')
	writer.append_data(image)
	for line in result.split('\n'):
		if (file_name + '.') in line:
			print(line)
			generate_qrcode(line, file_type)
			image = imageio.imread(line + '.png')
			writer.append_data(image)


