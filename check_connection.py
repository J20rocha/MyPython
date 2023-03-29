import urllib.request as urllib
import webbrowser


def main(url):
    print("Checking connectivity...")

    response = urllib.urlopen(url)
    print("Connected to ", url, " succesfully")
    print("The response code is ", response.getcode())
    try:
        webbrowser.open(url)
    except webbrowser.Error:
        print("Unable to open the requested url in the default browser")


print("This is a site connectivity program")
import_url= input("Input the url of the site ")
complete_url= "https://www."+str(import_url)

main(complete_url)
