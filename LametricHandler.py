from BaseHTTPServer import BaseHTTPRequestHandler

class LametricHandler(BaseHTTPRequestHandler):
	
	def __init__(self):
		print "constructor"
		BaseHTTPRequestHandler(self)
	
	def testtest(self):
		return

	#def do_GET(self):
	#	print self.path
	#	self.send_response(200)
	#	self.send_header('Content-Type', 'application/json')
	#	self.end_headers()
	#	return
