import zipfile
with zipfile.ZipFile('D:\\zip\\ccvt.zip', 'r') as zip_ref:
zip_ref.extractall()
