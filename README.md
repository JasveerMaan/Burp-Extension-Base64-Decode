# Burp-Extension-Base64-Decode

During the assessment timeframe, I noticed that the web application sneds base64 encoded message. Since there's multiple message being sent to the server under parmater "search", I decided to write Burp extension that converts my plaintext message (From Repeater, Scanner etc) to Base64. This allows me to use Repeater and Scanner feature from Burp Suite.

A web application sends base64 encoded HTTP Body to the server. Since multiple message being sent to the server under parmater "search", I wrote this Burp Suite extensions which allows me to send plaintext (HTTP Body) to the server. This allows me to use Burp Suite feature such as Repeater, Intruder and Scanner. 

#To do
1. Implement multithreading
