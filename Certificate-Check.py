import OpenSSL
import ssl
import socket
#import dns.resolver

def NameCheck(domain):
    #This will do a name look up to verify the FQDN
    # Get the IP of the FQDN
    try:
        host_ip = socket.gethostbyname(domain)
        print("FQDN",domain, "validated.  Returns IP address", host_ip)
        certcheck(domain)
    except socket.gaierror:
        # this means could not resolve the host
        print("FQDN ", domain, "error with name resolution.  Skipping cert check for",domain)
        print(" ")
    return()

def certcheck(domain):
    # get domain
    # get SSL Cert info
    cert = ssl.get_server_certificate((domain, 443))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    x509info = x509.get_notAfter()
    exp_day = x509info[6:8].decode('utf-8')
    exp_month = x509info[4:6].decode('utf-8')
    exp_year = x509info[:4].decode('utf-8')
    exp_date = str(exp_month) + "-" + str(exp_day) + "-" + str(exp_year)
    print("SSL Certificate for domain", domain, "will be expired on ", exp_date)
    print(" ")
    return ()
if __name__ == '__main__':
    myfile = open("list.txt", "r")
    item = myfile.readline()
    while item:
        myURL = str.rstrip(item)
        NameCheck(myURL)
        item = myfile.readline()
        if len(item) == 0: break
    myfile.close()