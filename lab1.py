import requests
while 1:
 url = input('Παρακαλω δωστε ενα url:')
 if url == '': break
 if not url.startswith('http'):
    url = 'http://'+ url
 try:
    with requests.get(url) as response:
        print("\nRESPONSE STATUS: ", response.status_code)
        print("RESPONSE HEADER")
        for key, value in response.headers.items():
            print("{:30s} {}".format(key, value))
        
        server = response.headers.get('Server')
        
        if server:
           print(f'Ο server που χρησιμοποιειται ειναι {server}')
        else:
           print('Δεν εντοπιζεται ο server :(')
        
        cookies = response.headers.get('set-cookie')
        if cookies:
            print('Παρακατω φαινονται τα cookies: \n',cookies)
        else:
           print('Δεν υπαρχουν cookies :( ')
        


 except:
    print('Λαθος,ισως δεν ειναι σωστο το link:', url)