f=open("settings.txt","r")
settings = {}
for line in f:
	line=line.strip()
	if not line.startswith('#') and len(line) > 0:
		key ,value = line.strip().split('=')
		settings[key.strip()] =value.strip()
f.close()
print(settings)

print(settings.get('tmp_table_size'))