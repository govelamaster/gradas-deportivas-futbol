#!/usr/bin/env python3
"""Grupo D: 30 ciudades programáticas /gradas-deportivas-en-{slug}/."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _make_spoke import SRC, transform

ROOT = "/Users/olgagovela/Library/CloudStorage/GoogleDrive-govelamaster@gmail.com/My Drive/Proyectos/gradas-deportivas-futbol"

CITIES = [
  ("cdmx", "CDMX", "Ciudad de México", "CDMX"),
  ("monterrey", "Monterrey", "Monterrey, Nuevo León", "Nuevo León"),
  ("guadalajara", "Guadalajara", "Guadalajara, Jalisco", "Jalisco"),
  ("puebla", "Puebla", "Puebla de Zaragoza, Puebla", "Puebla"),
  ("toluca", "Toluca", "Toluca, Estado de México", "Estado de México"),
  ("leon", "León", "León, Guanajuato", "Guanajuato"),
  ("queretaro", "Querétaro", "Santiago de Querétaro, Querétaro", "Querétaro"),
  ("merida", "Mérida", "Mérida, Yucatán", "Yucatán"),
  ("tijuana", "Tijuana", "Tijuana, Baja California", "Baja California"),
  ("saltillo", "Saltillo", "Saltillo, Coahuila", "Coahuila"),
  ("cancun", "Cancún", "Cancún, Quintana Roo", "Quintana Roo"),
  ("veracruz", "Veracruz", "Veracruz, Veracruz", "Veracruz"),
  ("chihuahua", "Chihuahua", "Chihuahua, Chihuahua", "Chihuahua"),
  ("hermosillo", "Hermosillo", "Hermosillo, Sonora", "Sonora"),
  ("aguascalientes", "Aguascalientes", "Aguascalientes, Aguascalientes", "Aguascalientes"),
  ("culiacan", "Culiacán", "Culiacán, Sinaloa", "Sinaloa"),
  ("san-luis-potosi", "San Luis Potosí", "San Luis Potosí, S.L.P.", "San Luis Potosí"),
  ("pachuca", "Pachuca", "Pachuca, Hidalgo", "Hidalgo"),
  ("morelia", "Morelia", "Morelia, Michoacán", "Michoacán"),
  ("villahermosa", "Villahermosa", "Villahermosa, Tabasco", "Tabasco"),
  ("tampico", "Tampico", "Tampico, Tamaulipas", "Tamaulipas"),
  ("reynosa", "Reynosa", "Reynosa, Tamaulipas", "Tamaulipas"),
  ("mexicali", "Mexicali", "Mexicali, Baja California", "Baja California"),
  ("torreon", "Torreón", "Torreón, Coahuila", "Coahuila"),
  ("acapulco", "Acapulco", "Acapulco, Guerrero", "Guerrero"),
  ("tuxtla-gutierrez", "Tuxtla Gutiérrez", "Tuxtla Gutiérrez, Chiapas", "Chiapas"),
  ("durango", "Durango", "Durango, Durango", "Durango"),
  ("xalapa", "Xalapa", "Xalapa, Veracruz", "Veracruz"),
  ("cuernavaca", "Cuernavaca", "Cuernavaca, Morelos", "Morelos"),
  ("oaxaca", "Oaxaca", "Oaxaca de Juárez, Oaxaca", "Oaxaca"),
]

def cfg(slug_city, short, full, estado):
    slug = f"gradas-deportivas-en-{slug_city}"
    return {
        "slug": slug,
        "title": f"Gradas Deportivas en {short} | Envío e Instalación | Sportmaster",
        "desc": f"Gradas deportivas en {full}: 12 modelos con techo, capacidad 35 a 150 personas. Envío e instalación a {short} en 4 a 6 semanas. Cotiza por WhatsApp en 1 a 2 horas.",
        "kw": f"gradas deportivas en {short.lower()}, gradas para canchas en {short.lower()}, gradas {short.lower()}, fabricante gradas {short.lower()}, venta gradas deportivas {short.lower()}, gradas escolares {short.lower()}, gradas inifed {short.lower()}, tribunas para canchas {short.lower()}",
        "og_t": f"Gradas Deportivas en {short} · Envío e Instalación | Sportmaster",
        "og_d": f"Gradas deportivas en {full}. 12 modelos. Envío e instalación. INIFED disponible.",
        "tw_t": f"Gradas Deportivas en {short} | Sportmaster",
        "tw_d": f"Gradas deportivas en {short}: 12 modelos. Envío e instalación.",
        "bread": f"Gradas Deportivas en {short}",
        "eyebrow": f"Envío e instalación en {short} · {estado}",
        "h1_pre": "Gradas<br>deportivas en<br>",
        "h1_acento": short,
        "h1_post": ".",
        "sub": f"Fabricamos y enviamos gradas deportivas a <strong>{full}</strong>: 12 modelos con techo, capacidad <strong>35 a 150 personas</strong>, modelo INIFED para escuelas públicas, opciones modulares para clubes y eventos.<br><br>Cotización en 1 a 2 horas por WhatsApp.",
        "wa_msg": f"Hola!%20Quiero%20cotizar%20gradas%20deportivas%20en%20{short.replace(' ','%20')}%20-%20vengo%20de%20gradasdefutbol.mx",
        "bestsellers_eyebrow": f"Más vendidas en {short}",
        "bestsellers_h2": f"Los 3 modelos más enviados a {short}",
        "beneficios_h2": f"Gradas deportivas con envío e instalación en {short}.",
        "faq_h2": f"Preguntas frecuentes · Gradas deportivas en {short}",
        "faq1_q": f"¿Sportmaster envía e instala gradas deportivas en {short}?",
        "faq1_a": f"Sí. Enviamos gradas deportivas a {full} y a todo el estado de {estado}. La fabricación toma 4 a 6 semanas desde la confirmación del pedido. El costo del flete se cotiza por destino final dentro del estado. También coordinamos la instalación en sitio para clientes en {short} y municipios vecinos: escuelas, clubes, hoteles, municipios y particulares.",
        "alt_kw": f"Gradas deportivas en {short}",
    }

def main():
    src = open(SRC).read()
    for slug_city, short, full, estado in CITIES:
        sp = cfg(slug_city, short, full, estado)
        out_dir = f"{ROOT}/{sp['slug']}"
        os.makedirs(out_dir, exist_ok=True)
        with open(f"{out_dir}/index.html", "w") as f:
            f.write(transform(src, sp))
        print(f"  ✓ /{sp['slug']}/")
    print(f"\n✓ {len(CITIES)} ciudades.")

if __name__ == "__main__":
    main()
