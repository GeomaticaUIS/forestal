import http.server
import socketserver

# Establece el directorio raíz del servidor
directorio_raiz = "./"

# Puerto en el que se ejecutará el servidor
puerto = 80#00

# Crea un objeto de manejador para el servidor
manejador = http.server.SimpleHTTPRequestHandler

# Configura el servidor
with socketserver.TCPServer(("", puerto), manejador) as servidor:
    print(f"Servidor iniciado en el puerto {puerto}. Presiona Ctrl+C para detener.")
    servidor.serve_forever()
