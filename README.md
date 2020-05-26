The dig command is a powerful command line DNS utility to research and troubleshoot domain name resolution. It is popular due to its flexibility, simplicity, and clear output. Included with Linux and Unix distributions, dig is most commonly used to:

- Performs DNS lookups
- Find host addresses, IP address, mail exchanges (MX), CNAMEs, name servers, and more
- Verify ISP DNS server and Internet connectivity
- Verify spam, blacklisting records, and more.

The mass-dig script ("dig_domain_to_ip.py") has two main functions:

single_domain_to_ip:
 - Expects a single domain and outputs to screen. Useful for testing purposes.
 
bulk_domain_to_ip:
 - Expects a filename containing domains and outputs to a timestamped file.

To select the desired function, simply uncomment your query type at the bottom of the script file. 

The initial purpose of the script was to filter and return just the IP Address of the given domain(s). The script includes an IP validation function to account for some domains returning canonical names (even when using ‘+short’ or ‘A Record’ flags within dig). There is also a customizable, randomized sleep interval between each dig query to prevent bulk query throttling. 
