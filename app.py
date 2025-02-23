from flask import Flask, render_template
import folium

app = Flask(__name__)

def generar_mapa():
    # Coordenadas de Saltillo
    lat, lon = 25.4383, -100.9737  
    mapa = folium.Map(location=[lat, lon], zoom_start=13)

    # Guardamos el mapa en un archivo HTML dentro de "templates"
    mapa.save("templates/mapa.html")

@app.route("/")
def home():
    generar_mapa()  # Genera el mapa antes de renderizar
    return render_template("index.html")

@app.route("/mapa")
def mostrar_mapa():
    return render_template("mapa.html")

if __name__ == "__main__":
    app.run(debug=True)
