\title{COMP 5970/6970: HTTP Reverse Shell}
\author{Alex Lewin, Charlie Harper}
\date{11/8/19}

\maketitle

### 1 Executive Summary

The purpose of this project was to develop and demonstrate our understanding of socket programming, The TCP/IP protocol suite, HTTP, and reverse-shell attacks.  In addition, the project had us focus on vulnerabilitity assessment on windows machines, and exercising information exfiltration frmo target machines. 

Our assignment was to pose as a malicious actor aiming to steal data from victims without detection. To do this, we wrote a python script that creates an HTTP reverse shell connection with a victim machine whom downloads our executable from a malicious website we have created. The script then collects information from the victim and sends it back to the server.

We were also able to successfully exfiltrate the information from the victim host and completely bypass Windows Defender.  


Our assignment was to pose as a malicious actor that aims to steal data from their victim. To do this, we were instructed to write a python script that creates an HTTP reverse shell connection between our host machine and a remote windows client. This script should collect the victim's operating system registry contents into a file and then send the file back to our host machine.  



## 2 Problem Description

### 2.1 Overview

Between socket programming, TCP protocol, HTTP, and reverse-shell attacks.  

Our assignment was to pose as a malicious actor aiming to steal data from their victim. To do this, we were instructed to write a python script that creates an HTTP reverse shell connection between our host machine and a remote windows client.  

This script should be  converted into an executable file and sent to the victim machine. Once the script was downloaded and ran on the victim machine, it should access the key data from the Windows registry. Then, the data should be collected into a file and exfiltrated to the attacker.  

This script should collect the victim's operating system registry contents into a file and then exfiltrate the data back to our host machine. In addition, our script must be obfuscated to bypass Windows Defender and leave no trace otherwise.  

There are quite a few repeating sentences - we may want to reword them.

### 2.2 Technical Specifications

###### Server (Attacker) machine specifications:

   - Operating System: Kali Linux  
   - Server Location: Shelby 2129  
   - IP Address: 192.168.x.30  
   - `python3 --version`: `Python 3.6.7`  


###### Client (victim) machine specifications:   

   - Operating System: Microsoft Windows 10  
   - Server Location: Shelby 2129
   - IP Address: 192.168.x.40  
   - `python3 --version`: `Python 3.6.7`  

### 2.3 Scripts 

To accomplish this goal, we created two independent python scripts:  

   1. `server.py`: This script runs on the attacker machine. It serves as an http server sitting on top a TCP listener. We have defined customer GET and POST functionality, that will pass commands to the target machine upon connectionIn addition, it handles file transfers from the victim machine. 
   2. `client.py`: This script was sent to the victim machine. The serves as an http client and sits on top of a TCP client socket. This client sends GET and POST requests to the server, runs arbitrary code, pulls registry information, and passes files/data to the server/attacker machine.


## 3 Code Explanation  

To orchestrate the reverse shell connection, we created two scripts: `client.py` ran on the victim machine and `server.py` ran on our host machine.  

### 3.1 `server.py`

On the `server.py` script, we used several external python modules:  

   1. All of the socket programming was done using the `socket` module.  
   2. To communicate between the two systems over a HTTP connection, we utilized the `SimpleHTTPRequestHandler` in the `http.server` module.  
   3. To receive and handle TCP requests, we used the `socketserver` module.
   4. Finally, we used the `sys` module to call `sys.exit`.

```python
import socket as sock
import http.server as Serv
import socketserver
import sys
```

The `signal_handler` function allows run-time termination to occur.

```python
def signal_handler():
	print("crtl-c was hit")
	sys.exit(0)
```

## 6 Python Code to Executable form:


## 5 Obfuscation Efforts 

A goal of the project was to run this process without detection of the victim's antivirus software. This was easily done without having to obfuscate the source code or the behavior of the code itself. 

However, this begs the question: if the file had been detected by the antivirus of the victim machine, how would we get around it?

To get a foundation for where our code was as far as being detected by antivirus software, we ran it through VirusTotal.  Before doing anything to the executable, 9/40 tests/scans found the executable to be malicious software. After getting the foundation, several attempts and methods were explored to obfuscate and slip thoruhg antivirus software:

### 5.1 Base64 encoding and decoding

### 5.2 Obfuscating Strings and Obscuring Functions

### 5.3 Encryption


### 5.4 Obfuscation Conclusion

When fully implemented and layered, obfuscation may be a viable option to bypass or slip through antivirus software; however, when implementing a single simple method, obfuscation seems to have the opposite effect and actually trigger some of the antivirus scans - a specific example being with the base64 encoding and decoding.
I suspoect that many of the antivirus software vendors have become aware of the behaviors or techniques that authors of the malware are using to slip through antivirus. This has led many of them to look for those specific techniques and flag them as suspicious processes. In the future, I would like to try and implement the encryption method, and laer the obfuscation techniques to bypass TotalVirus' scanners. 
In addition, another method that was presented by the fireeye redteam was the inject bash commands into threads and memory instead of running the suspicious processes through the command prompt- this would be interesting the see in the future.

fireeye redteam antivirus article: https://www.fireeye.com/blog/threat-research/2019/10/staying-hidden-on-the-endpoint-evading-detection-with-shellcode.html



## 6 Conclusions



## 6 Recommendations
