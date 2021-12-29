f = open('rosalind_gc.txt')
lines = f.readlines()
name = ''
content = ''
dnas = dict()
for line in lines:
    line = line.strip()
    if line.startswith('>'):
        dnas[name] = content
        name = line.replace('>', '')
        content = ''
        continue
    content += line
dnas[name] = content

id = ''
gc_content = 0
for key, value in dnas.items():
    value = value.strip()
    if not key.startswith('Rosalind_'):
        continue
    count = value.count('G')+value.count('C')
    percentage = round((count/len(value))*100, 6)
    if percentage > gc_content:
        id = key
        gc_content = percentage
print(id)
print(gc_content)
