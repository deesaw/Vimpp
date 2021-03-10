f=open("settings.txt","r")
settings = {}
for line in f:
	if "=" in line:
		key ,value = line.strip().split('=')
		settings[key.strip()] =value.strip()
f.close()
print(settings)

print(settings.get('tmp_table_size'))
