import os, sys
home = os.path.expanduser('~') + "/"
env = home + 'env/'
bash = env + 'bash/'
profile = env + '.profile_init'
time = env + '.date'

s = ""
for t in os.listdir(bash):
	with open(bash + t) as f:
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
with open(profile, "w+") as f:
	f.write("\n".join(s))

with open(time, "w+") as f:
	f.write(sys.argv[1])
