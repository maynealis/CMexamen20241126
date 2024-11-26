from http.server import HTTPServer , BaseHTTPRequestHandler
from jinja2 import Template
import urllib.parse

def genera_html_base(title):
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
    

def genera_index(user_initials = ""):
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
            <input type="text" id="base" name="base"><br>
            <label for="lado2">Altura:</label><br>
            <input type="text" id="altura" name="altura"><br>
            <input type="submit" value="Calcular">
        </form>

    </body>
    </html>
    """
    html_content = genera_html_base("Calcula área") + html_body
    return html_content

def genera_resultado(base, altura):
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
    html_content = genera_html_base("Resultado") + html_body
    return html_content

    

    