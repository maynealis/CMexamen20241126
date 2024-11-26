from http.server import HTTPServer , BaseHTTPRequestHandler
from jinja2 import Template
import urllib.parse

def get_html_base(title):
    """Devuelve un string con el html correspondiente al header.

    Args:
        title (str): Título de la página

    Returns:
        str: Html correspondiente al header de una página
    """
    return f"""
    <!DOCTYPE html>
    <html lang="es">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>
        </head>
    """
    
def get_html_index(user_initials = ""):
    """Devuelve un string con el html correspondiente a la página principal con un formulario para introducir base y altura de un triángulo.

    Args:
        user_initals (str): Iniciales del alumno/usuario

    Returns:
        str: html correspondiente a la página principal para calcular el área de un triángulo, incluyendo el html básico.
    """
    html_body = f"""
    <body>
        <h1>
            Calculador de Área de Triángulos de {user_initials}
        </h1>
        <form action="/resultado" method="post">
            <label for="base">Base:</label><br>
            <input type="text" id="base" name="base" required><br>
            <label for="lado2">Altura:</label><br>
            <input type="text" id="altura" name="altura" required><br>
            <input type="submit" value="Calcular">
        </form>

    </body>
    </html>
    """
    html_content = get_html_base("Calcula área") + html_body
    return html_content

def get_html_result(base, altura):
    """Devuelve un string con el html correspondiente a la página resultado donde visualizar el cálculo del área de un triángulo.

    Args:
        base (float): Valor de la base del triángulo
        altura (float): Valor de la altura del triángulo

    Returns:
        str: html correspondiente a la página para visualizar el resultado del cálculo, incluyendo el html básico.
    """
    html_body = f"""
    <body>
        <h1>El resultado del area del triángulo de lados { base } y { altura } es { base*altura/2 }</h1>
    </body>
    </html>
    """
    html_content = get_html_base("Resultado") + html_body
    return html_content

    
class CustomBaseHTTPRequestHandler(BaseHTTPRequestHandler):
    """Clase que crea un RequestHandler personalizado que hereda de BaseHTTPRequestHandler para gestionar los GET y POST al servidor.

    Args:
        BaseHTTPRequestHandler (class): clase de la que hereda
    """

    def write_html(self, html_content):
        """Envía un html para que se muestre en el navegador.

        Args:
            html_content (str): html en formato str
        """
        # Código 200 significa que todo ha ido correcto
        self.send_response(200)
        # Enviamos en la cabezera el tipo de contenido que ser enviará en el cuerpo. En este caso de tipo html
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Escribimos el contenido del cuerpo, codificando en utf-8 para que se muestren los acentos.
        self.wfile.write(bytes(html_content, 'utf-8'))
    

    def do_GET(self):
        """Método que maneja una petición GET al servidor. 
        Usamos la función write_html para enviar los headers y el contenido que en este caso será el formulario para calcular el área de un triángulo como respuesta.
        """
        self.write_html(get_html_index("CM"))
        

    def do_POST(self):
        """Método que maneja una petición POST al servidor.
        Obtenemos los valores de base y altura del formulario a través de los params y usamos write_html para enviar el html de resultado como respuesta.
        """
        # Obtenemos el tamaño de los headers
        content_length = int(self.headers.get('Content-Length'))
        post_data = self.rfile.read(content_length)
        # Decodificamos los argumentos que recibimos de la misma forma que los codificamos
        params = urllib.parse.parse_qs(post_data.decode('utf-8'))
        # Obtenemos los valores del diccionario de respuesta
        base = float(params['base'][0])
        altura = float(params['altura'][0])
        
        self.write_html(get_html_result(base, altura))
    


if __name__ == "__main__":
    server_name = "localhost"
    server_port = 3001
    with HTTPServer((server_name, server_port), CustomBaseHTTPRequestHandler) as httpd:
        print(f"Servidor en http://{server_name}:{server_port}")
        try: 
            httpd.serve_forever()
        except KeyboardInterrupt:
            # keyboard interrupt in terminal (Ctrl+C)
            print("\nDeteniendo el servidor...")
            httpd.shutdown()
            print("Servidor parado")
    

    

    