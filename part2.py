from flask import Flask
from flask import jsonify
import multiprocessing
from psutil import virtual_memory
import socket
app = Flask(__name__)

@app.route('/')
def display():
    return "Looks like it works!"
@app.route('/status')
def status():

	hostname = socket.gethostname()
	ip =  socket.gethostbyname(hostname)
	cpus = multiprocessing.cpu_count()
	mem = virtual_memory()
	memtotal = mem.total / 1073741824
	dict = {'hostname':hostname,'ip address': ip,'cpus':cpus,'memory':memtotal}
	return jsonify(dict)
	
if __name__=='__main__':
    app.run(port=8080)