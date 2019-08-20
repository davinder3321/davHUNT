import requests
print ("Hello Cyber SOC Analyst")
print ("Welcome to DAVHUNT")

print ('''
Owner Details : Davinder Pal Singh
Website : davindertutorials.com
Contact : 9988663321 || 8360942792
Email: davindersingh26793@gmail.com

DESCRIPTION : What you will get >>
>>>>>VirusTotal Result
>>>>>DNS Lookup
>>>>>Whois Lookup
>>>>>Revrse IP Lookup
>>>>>GeoIP Lookup
>>>>>subnet Lookup
>>>>>Port Scanner
>>>>>Extract Links
>>>>>Zone Transfer
>>>>>HTTP Header
>>>>>Host Finder
>>>>>IP-Locator

''')
url = input("Enter the Target Hostname >>>> \n" )
print("Your Entered Target is : " + url);
print("\n")

print("Information Gathering Starts for the target  : " + url);
print("\n")

############VIRUS TOTAL ###################
virusurl = 'https://www.virustotal.com/vtapi/v2/url/report'
params = {'apikey': '894fd4ac8941b97aacb2ac494b0347d9aae2daf7c4880a64ab57e3394e0947fc', 'resource':url}
response = requests.post(virusurl, data=params)
result = response.json()
for i,j in result.items():
    print (i)
    print (j)


############whois details###################
print("WHOIS Details for the target website: \n")
whois = "http://api.hackertarget.com/whois/?q=" + url
response = requests.get(whois)
print(response.text)
print("\n")

#############Reverse IP details###################
print(" Reverse IP LookUP Details for the target website: \n")
reverse = "http://api.hackertarget.com/reverseiplookup/?q=" + url
response = requests.get(reverse)
print(response.text)
print("\n")

#############DNS details###################
print(" DNS Details for the target website: \n")
dns = "http://api.hackertarget.com/dnslookup/?q=" + url
response = requests.get(dns)
print(response.text)
print("\n")

#############Geo IP details###################
print(" Geo IP Details for the target website: \n")
geo = "http://api.hackertarget.com/geoip/?q=" + url
response = requests.get(geo)
print(response.text)
print("\n")

#############Subnet Lookup details###################
print(" Subnet LookUP for the target website: \n")
sub = "http://api.hackertarget.com/subnetcalc/?q=" + url
response = requests.get(sub)
print(response.text)
print("\n")

#############Port Scanning ##################
print(" Port Scanning for the target website: \n")
port = "http://api.hackertarget.com/nmap/?q=" + url
response = requests.get(port)
print(response.text)
print("\n")


############# Extract Links##################
print(" Extract Links for the target website: \n")
get = "https://api.hackertarget.com/pagelinks/?q=" + url
response = requests.get(get)
print(response.text)
print("\n")

############# Zone Transfer Details ##################
print(" Zone Transfer Details  for the target website: \n")
zone = "http://api.hackertarget.com/zonetransfer/?q=" + url
response = requests.get(zone)
print(response.text)
print("\n")


############# HTTP Header Details ##################
print(" HTTP Header Details  for the target website: \n")
header = "http://api.hackertarget.com/httpheaders/?q=" + url
response = requests.get(header)
print(response.text)
print("\n")


############# Host Finder Details ##################
print(" Host Finding  for the target website: \n")
host = "http://api.hackertarget.com/hostsearch/?q=" + url
response = requests.get(host)
print(response.text)
print("\n")

############# IP Locater Details ##################
print(" IP Locater for the target website: \n")
locate = "http://ip-api.com/json/" + url
response = requests.get(locate)
print(response.text)
print("\n")

input("PRESS ENTER TO CLOSE")