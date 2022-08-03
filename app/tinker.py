import http.server #Deixa criar um servidor
import socketserver #"ouve" o que é jogado na API

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler # Reqisição simples HTTP
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print("Servidor local funcionando")
    print()
    httpd.serve_forever() #Loop