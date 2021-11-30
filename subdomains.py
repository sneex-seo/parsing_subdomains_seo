import requests
import socket
import csv

with open("domains.txt", 'r+', encoding='utf-8') as f:
    domains = [line.strip() for line in f]

file = open("subdomains.txt")
# read all content
content = file.read()
# split by new lines
subdomains = content.splitlines()

# a list of discovered subdomains
discovered_subdomains = []
subdomain_ips = []
for domain in domains:
    domain = domain.replace("http://", "")
    domain = domain.replace("https://", "")
    domain = domain.replace("www.", "")
    print("check subdomains for: " + domain)
    for subdomain in subdomains:
        # construct the url
        url = f"http://{subdomain}.{domain}"
        try:
            # if this raises an ERROR, that means the subdomain does not exist
            requests.get(url)
        except requests.ConnectionError:
            # if the subdomain does not exist, just pass, print nothing
            pass
        else:
            # append the discovered subdomain to our list
            discovered_subdomains.append(url)
            regex_IP = url.replace("http://","")
            IP = socket.gethostbyname(regex_IP)
            print("[+] Discovered subdomain:", url, "[+] Discovered IP:", IP)
            subdomain_ips.append(IP)
            # save the discovered subdomains into a file
            result_file = open('Subdomain+IP.csv', 'a', encoding="UTF-8")
            result_file.write(f'{url}\t{IP}\n')
            result_file.close()


