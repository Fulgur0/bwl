import requests
import json

with open('bwl/dns.json', 'r') as f:
    dns = json.load(f)

def get_ip(domain):
    args = domain.split('.')
    if len(args) < 2:
        return 'Invalid domain'
    try:
        dns_server = dns[args[-1]]
    except:
        return 'No DNS server found for ' + args[-1]
    domain = '.'.join(args[-2:])
    print("DNS server for '" + args[-1] + "' " + dns_server)
    try:
        r = requests.get(dns_server + "/" + domain)
        return json.loads(r.text)
    except:
        return 'Failed to connect to DNS server'
