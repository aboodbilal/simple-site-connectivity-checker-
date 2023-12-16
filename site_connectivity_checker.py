import urllib.request as urllib

def main(url):
    print("Checking connectivity...  ")

    respons = urllib.urlopen(url)
    print("connected to ",url,"succefully")
    print("the response code was : ", respons.getcode())


print("this is a site connectivity checker program")
input_url= input("input the url of the site that you want to check")
main(input_url)


    