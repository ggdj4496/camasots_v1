import http.server, socketserver, os
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
os.chdir(r'C:\Users\X\Desktop\VIRGILIO_CORE')
print(f'🏛️ VIRGILIO_CORE: Portal abierto en http://localhost:{PORT}')
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    httpd.serve_forever()
