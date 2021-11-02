import os, zipfile

path = r'C:\Users\jstangle\Desktop\submissions'
extension = ".zip"

os.chdir(path) # change directory from working dir to dir with files

for folder in os.listdir(path):
    zipf = zipfile.ZipFile('{0}.zip'.format(os.path.join(path, folder)), 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(os.path.join(path, folder)):
        for filename in files:
            zipf.write(os.path.abspath(os.path.join(root, filename)), arcname=filename)
    zipf.close()