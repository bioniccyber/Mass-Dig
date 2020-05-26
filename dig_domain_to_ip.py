#!/usr/bin/python3

import ipaddress
import sys
import subprocess
from random import randint
import time
from time import sleep

# Function to Process a Single Domain - PRINTS OUTPUT TO SCREEN
def single_domain_to_ip():
    domain = sys.argv[1]
    dig_output_list = subprocess.getoutput("dig +short " + domain).splitlines()
    for dig_record in dig_output_list:
        try:
            # Using 'ipaddress' library (https://docs.python.org/3/library/ipaddress.html), validate IP Address
            ipaddress.ip_address(dig_record)
            print (domain + " #~# " + dig_record)
        except:
            pass

# Function to Process Domains in Bulk by File - SAVES OUTPUT TO FILE
def bulk_domain_to_ip():

    # Filename of output
    date = time.strftime("%m-%d-%Y")
    output_filename = date + "_output_dig.txt"

    dom_file = sys.argv[1]
"dig_domain_to_ip.py" 51L, 2055C                                                                      1,1           Top
import ipaddress
import sys
import subprocess
from random import randint
import time
from time import sleep

# Function to Process a Single Domain - PRINTS OUTPUT TO SCREEN
def single_domain_to_ip():
    domain = sys.argv[1]
    dig_output_list = subprocess.getoutput("dig +short " + domain).splitlines()
    for dig_record in dig_output_list:
        try:
            # Using 'ipaddress' library (https://docs.python.org/3/library/ipaddress.html), validate IP Address
            ipaddress.ip_address(dig_record)
            print (domain + " #~# " + dig_record)
        except:
            pass

# Function to Process Domains in Bulk by File - SAVES OUTPUT TO FILE
def bulk_domain_to_ip():

    # Filename of output
    date = time.strftime("%m-%d-%Y")
    output_filename = date + "_output_dig.txt"

    dom_file = sys.argv[1]
    with open(dom_file) as domain_file:
            for domain in domain_file:
                # File can contain trailing whitespace or newlines. Remove them using 'rstrip'
                domain = domain.rstrip()
                # Sleep in random intervals provided (currently set anywhere from 2-7 seconds) - in effort to try and not get blocked by bulk dig queries
                sleep(randint(2,7))
                # Use Dig Command
                dig_output_list = subprocess.getoutput("dig +short " + domain).splitlines()
                for dig_record in dig_output_list:
                    try:
                        # Using 'ipaddress' library (https://docs.python.org/3/library/ipaddress.html), validate IP Address
                        ipaddress.ip_address(dig_record)
                        with open(output_filename, 'a') as f:
                            f.write(domain + " #~# " + dig_record + '\n')
                            #print (domain + " #~# " + dig_record)
                    except:
                        pass
    domain_file.close()

# Uncomment ONLY 1 of the following to either process a single domain or process by file
#single_domain_to_ip()
bulk_domain_to_ip()
