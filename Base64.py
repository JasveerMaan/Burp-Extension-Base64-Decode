import base64
from burp import IBurpExtender, IHttpListener

class BurpExtender(IBurpExtender, IHttpListener):

	def registerExtenderCallbacks(self, callbacks):
		self.callbacks = callbacks
		self.helpers = callbacks.getHelpers()
		callbacks.registerHttpListener(self)
		callbacks.setExtensionName("Base64 Decoder")

	def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
		#Only the following tools are allowed
		if toolFlag != self.callbacks.TOOL_REPEATER and toolFlag != self.callbacks.TOOL_SCANNER and toolFlag != self.callbacks.TOOL_EXTENDER and toolFlag != self.callbacks.TOOL_INTRUDER:
			return

		if (messageIsRequest):
			request = messageInfo.getRequest()
			requestHTTPService = messageInfo.getHttpService();
			requestInfo = self.helpers.analyzeRequest(requestHTTPService,request)

			captured_headers = requestInfo.getHeaders()
			body = request[requestInfo.getBodyOffset():]
			body = self.helpers.bytesToString(body)
			
			for headers in captured_headers:
				if "127.0.0.1" in headers:
					flag = True

			if flag:
				#Taking value after search=
				value_in_parameter = body.split("search=",1)[1]
				#Will print value in Extender tab - Debug purpose
				print "[*] Printing value in search parameter:"
				print value_in_parameter
				#Encoding
				encode_value = base64.b32encode(value_in_parameter)
				new_body = "search="+encode_value
				#Debug purpose
				print "[*] Printing encoded value:"
				print new_body

			updatedRequest = self.helpers.buildHttpMessage(captured_headers, new_body)
			messageInfo.setRequest(updatedRequest)
			print("Done!")