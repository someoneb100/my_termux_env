import os
bash = os.path.expanduser('~') + "/env/"
bash, profile = bash + 'bash/', bash + '.profile_init'

export, alias, rest = [],[],[]
for f in os.listdir(bash):
	with open(bash + f, "r") as f:
		for l in f:
			l = l.rstrip()
			if not l: continue
			elif 'export' in l: export.append(l)
			elif 'alias' in l: alias.append(l)
			else: rest.append(l)

with open(profile, "w+") as f:
	f.write("\n".join(export + alias + rest))
