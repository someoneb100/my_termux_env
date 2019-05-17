import os, sys
home = os.path.expanduser('~')
env = home + '/env'
bash = env + '/bash'
profile = env + '/.profile_init'
t = env + '/.date'

with open(t, "w+") as f:
	f.write(sys.argv[1])

s = ""
for t in os.listdir(bash):
	with open(t) as f:
		t = f.read()
		s += t

s = s.split('\n')
export, alias, rest = [],[],[]
for t in s:
	f = t.split(' ')
	if 'export' in f: export.append(t)
	elif 'alias' in f: alias.append(t)
	else: rest.append(t)

s = export + alias + rest
with open(profle, "w+") as f:
	f.write(s.join("\n"))
