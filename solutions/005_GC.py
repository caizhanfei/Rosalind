f = open('data.fasta')
lines = f.readlines()
name = ''
content = ''
dnas = dict()
for line in lines:
    if line.startswith('>'):
        dnas[name] = content
        name = line.replace('>', '')
        content = ''
        continue
    content += line
print(dnas)
