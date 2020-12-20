# Burp-Extension-Base64-Decode

During the assessment timeframe, I noticed that the web application sneds base64 encoded message. Since there's multiple message being sent to the server under parmater "search", I decided to write Burp extension that converts my plaintext message (From Repeater, Scanner etc) to Base64. This allows me to use Repeater and Scanner feature from Burp Suite.
