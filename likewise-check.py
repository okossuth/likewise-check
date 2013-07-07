#!/usr/bin/python

import os
import subprocess
import logging

def check():
    status = 0
    print "Checking AD connection status..."
    #execute lw-get-status
    p = subprocess.Popen('lw-get-status', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #parse status
    for line in p.stdout.readlines():
        if "Unknown" in line:   
            status = 1
        else:
            pass
    logging.basicConfig(filename='/var/log/likewise-check.log',level=logging.INFO,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    if status == 0 :
        print "AD connection working!"
        logging.info('Likewise-open AD connection working!')
        
    else:
        print "AD connection problems"
        logging.info('Likewise-open AD connection problems')

def main():
    print "Likewise Network status checker"
    check()

if __name__=='__main__':
    main()
