import http.server, socketserver, json

class VirgilioBubbleHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Este nodo recibe los datos de tus formularios de Bubble (deudas, fotos)
        if self.path == '/api/sync_bubble':
            self.send_response(200)
            self.end_headers()
            print("[!] DATOS RECIBIDOS DESDE LA APP BUBBLE.IO")
            
socketserver.TCPServer(('', 8081), VirgilioBubbleHandler).serve_forever()
