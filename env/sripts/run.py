#!/usr/bin/env python3

import os, sys, subprocess, time

class runner(object):

    def __init__(self, filename, arguments):
        self.filename = filename
        self._waitcount = 0
        self._cashed_stamp = 0
        if arguments != '':
            arguments = " " + arguments + " "
        extension = filename.split('.')[-1]
        
        #ide jednu po jednu extenziju
        if extension == 'sh':
            if filename[0] == '$':
                self.command = filename + arguments
            else:
                self.command = './' + filename + arguments
        elif extension == 'py':
            self.command = 'python3 ' + filename + arguments
        elif extension == 'c':
            self.command = 'gcc ' + filename + ' -o $TMP/temp && $TMP/temp' + arguments
        else:
            print('Nepodrzana extenzija! Program radi sa .sh, .py i .c kodovima')
            exit()


    def go(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cashed_stamp:
            self._cashed_stamp = stamp
            sys.stderr.write("\x1b[2J\x1b[H")
            sys.stderr.flush()
            subprocess.call(self.command, shell=True)
        else:
            if self._waitcount == 10:
                print("\r          \r.", end='', flush=True, file=sys.stderr)
                self._waitcount = 1
            else:
                print(".", end='', flush=True, file=sys.stderr)
                self._waitcount += 1

def main():
    script = runner(sys.argv[1], " ".join(sys.argv[2:]))
	
    while(True):
        try:
            time.sleep(1)
            script.go()
        except KeyboardInterrupt:
            print("\nGotovo! Dovidjenja...")
            break
        except:
            print("Nepredvidjena greska: {}".format(sys.exc_info()[0]))
            break

if  __name__ == "__main__":
    main()
