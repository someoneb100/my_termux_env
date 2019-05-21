#!/usr/bin/env python3

import os, sys, subprocess, time

class runner(object):

	def __init__(self, filename, arguments):
		self.filename = filename
		if arguments != '': arguments = " " + arguments
		extension = filename.split('.')[-1]
        
        #ide jednu po jednu extenziju
		if extension == 'sh':
			if filename[0] == '$': self.command = filename + arguments
			else: self.command = './' + filename + arguments
		elif extension == 'py':
			self.command = 'python3 ' + filename + arguments
		elif extension == 'c':
			self.command = 'gcc ' + filename + ' -o $TMPDIR/temp && $TMPDIR/temp' + arguments
		else:
			print('Nepodrzana extenzija! Program radi sa .sh, .py i .c kodovima')
			exit()
		self.command = self.command.split(' ')


	def __call__(self, mute=False):
		waitcount, cashed_stamp = 0, 0
		while(True):
			try:
				stamp = os.stat(self.filename).st_mtime
				if stamp != cashed_stamp:
					cashed_stamp = stamp
					if not mute:
						sys.stderr.write("\x1b[2J\x1b[H")
						sys.stderr.flush()
						subprocess.run(self.command)
					else: self.output = subprocess.run(self.command, stdout=subprocess.PIPE).stdout.decode("utf-8")
				elif not mute:
					if waitcount == 10:
						print("\r          \r.", end='', flush=True, file=sys.stderr)
						waitcount = 1
					else:
						print(".", end='', flush=True, file=sys.stderr)
						waitcount += 1
				time.sleep(1)
			except KeyboardInterrupt:
				print("\rGotovo! Dovidjenja...")
				break
			except:
				print("Nepredvidjena greska: {}".format(sys.exc_info()[0]))
				break

if  __name__ == "__main__":
	script = runner(sys.argv[1], " ".join(sys.argv[2:]))
	script()

