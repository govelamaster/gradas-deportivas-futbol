#!/usr/bin/env python3
"""Genera spokes programáticos a partir de la plantilla /precio-gradas-metalicas-mexico-2026/."""
import os, re, shutil

ROOT = "/Users/olgagovela/Library/CloudStorage/GoogleDrive-govelamaster@gmail.com/My Drive/Proyectos/gradas-deportivas-futbol"
SRC = f"{ROOT}/precio-gradas-metalicas-mexico-2026/index.html"

SPOKES = [
    {
        "slug": "gradas-techadas-modelos",
        "title": "Gradas Techadas en México | 12 Modelos con Techo · Sportmaster",
        "desc": "Gradas techadas con techo de lona, policarbonato o lámina galvanizada. 12 modelos para canchas deportivas, escuelas y clubes. Capacidad 35 a 150 personas. Cotiza por WhatsApp.",
        "kw": "gradas techadas, gradas cubiertas, gradas con techo, gradas techo curvo, gradas techo recto, gradas para canchas con techo, modelos gradas techadas, techo lona, techo policarbonato",
        "og_t": "Gradas Techadas · 12 Modelos para Canchas Deportivas en México",
        "og_d": "Gradas techadas en lona, policarbonato y lámina galvanizada. 12 modelos para fútbol 7, pádel y escuela. Acero estructural + INIFED.",
        "tw_t": "Gradas Techadas en México · 12 Modelos | Sportmaster",
        "tw_d": "Gradas con techo de lona, policarbonato o lámina galvanizada. 12 modelos. INIFED. Cotiza por WhatsApp.",
        "bread": "Gradas Techadas",
        "eyebrow": "Techo lona · policarbonato · lámina galvanizada",
        "h1_pre": "Gradas techadas<br>para canchas<br>",
        "h1_acento": "deportivas",
        "h1_post": ".",
        "sub": "12 modelos con techo curvo o recto: <strong>lona, policarbonato o lámina galvanizada</strong>. Protege a tu público del sol, lluvia y granizo. Capacidad de 12 a 150 personas.<br><br>Cotización en 1 a 2 horas por WhatsApp.",
        "wa_msg": "Hola!%20Quiero%20cotizar%20gradas%20techadas%20-%20vengo%20de%20gradasdefutbol.mx",
        "bestsellers_eyebrow": "Tipos de techo",
        "bestsellers_h2": "Los 3 modelos de gradas techadas más vendidos",
        "beneficios_h2": "Gradas con techo que protegen 365 días al año. Sin letra pequeña.",
        "faq_h2": "Preguntas frecuentes · Gradas techadas",
        "faq1_q": "¿Qué tipos de techo tienen las gradas techadas Sportmaster?",
        "faq1_a": "Ofrecemos 3 tipos de techo: <strong>lona</strong> (más económica, vida útil 8-10 años), <strong>policarbonato de 6mm</strong> (traslúcido, resistente a granizo, vida útil 15+ años, único INIFED) y <strong>lámina galvanizada</strong> (la más resistente, ideal para climas extremos y zonas costeras). El techo curvo es para 35 a 75 personas; el techo recto para 100 personas; el techo curvo de gran luz para 150 personas.",
        "alt_kw": "Gradas techadas",
    },
    {
        "slug": "gradas-techadas-con-techo-de-lona",
        "title": "Gradas Techadas con Techo de Lona en México | Sportmaster",
        "desc": "Gradas techadas con techo de lona para canchas deportivas. Opción más económica con protección solar y de lluvia. 6 modelos de 35 a 150 personas. Cotiza por WhatsApp.",
        "kw": "gradas techadas lona, gradas con techo lona, gradas techo curvo lona, gradas economicas con techo, gradas techo lona precio, gradas para canchas techo lona, gradas escolares lona, gradas con cubierta lona",
        "og_t": "Gradas Techadas con Techo de Lona · Canchas Deportivas México",
        "og_d": "Gradas con techo de lona: opción económica para fútbol 7, pádel y escuela. 6 modelos de 35 a 150 personas.",
        "tw_t": "Gradas Techadas con Techo de Lona | Sportmaster",
        "tw_d": "Gradas con techo de lona para canchas deportivas. 6 modelos económicos. Cotiza por WhatsApp.",
        "bread": "Gradas Techadas con Techo de Lona",
        "eyebrow": "Techo de lona · opción económica · 6 modelos",
        "h1_pre": "Gradas techadas<br>con techo de<br>",
        "h1_acento": "lona",
        "h1_post": ".",
        "sub": "La opción más económica con protección solar y de lluvia. <strong>6 modelos</strong> con techo curvo o recto de lona reforzada, capacidad de 35 a 150 personas. Vida útil de la lona 8 a 10 años.<br><br>Cotización en 1 a 2 horas por WhatsApp.",
        "wa_msg": "Hola!%20Quiero%20cotizar%20gradas%20techadas%20con%20techo%20de%20lona%20-%20vengo%20de%20gradasdefutbol.mx",
        "bestsellers_eyebrow": "Techo de lona",
        "bestsellers_h2": "Los 3 modelos con techo de lona más vendidos",
        "beneficios_h2": "Techo de lona: protección sin sobrecostos. Sin letra pequeña.",
        "faq_h2": "Preguntas frecuentes · Gradas techadas con techo de lona",
        "faq1_q": "¿Qué tan resistente es el techo de lona en gradas Sportmaster?",
        "faq1_a": "Nuestro techo de lona es reforzado para uso intemperie con protección UV y vida útil de <strong>8 a 10 años</strong>. Resiste sol, lluvia y vientos normales. Para zonas costeras, climas extremos o granizo recurrente, recomendamos techo de policarbonato o lámina galvanizada (más caros pero con mayor durabilidad). La lona se puede reemplazar al final de su vida útil sin cambiar la estructura.",
        "alt_kw": "Gradas techadas con techo de lona",
    },
    {
        "slug": "gradas-techadas-con-techo-de-policarbonato",
        "title": "Gradas con Techo de Policarbonato 6mm INIFED | Sportmaster",
        "desc": "Gradas techadas con techo de policarbonato de 6mm: traslúcido, resistente a granizo, único modelo INIFED. Capacidad 35 a 75 personas. Cotiza por WhatsApp.",
        "kw": "gradas techadas policarbonato, gradas con techo policarbonato, gradas techo policarbonato 6mm, gradas INIFED, gradas escolares INIFED, gradas con cubierta policarbonato, gradas policarbonato traslucido",
        "og_t": "Gradas con Techo de Policarbonato 6mm · INIFED",
        "og_d": "Gradas con policarbonato traslúcido resistente a granizo. Único modelo certificado INIFED para escuelas públicas.",
        "tw_t": "Gradas Techadas con Policarbonato INIFED | Sportmaster",
        "tw_d": "Techo policarbonato 6mm traslúcido. Único modelo INIFED. Cotiza por WhatsApp.",
        "bread": "Gradas Techadas con Techo de Policarbonato",
        "eyebrow": "Policarbonato 6mm · INIFED · 15+ años",
        "h1_pre": "Gradas techadas<br>con techo de<br>",
        "h1_acento": "policarbonato",
        "h1_post": ".",
        "sub": "Techo traslúcido de policarbonato de 6mm que deja pasar luz natural y resiste granizo. <strong>Única opción INIFED</strong> para canchas escolares públicas. Vida útil 15+ años.<br><br>Cotización en 1 a 2 horas por WhatsApp.",
        "wa_msg": "Hola!%20Quiero%20cotizar%20gradas%20techadas%20con%20policarbonato%20-%20vengo%20de%20gradasdefutbol.mx",
        "bestsellers_eyebrow": "Techo policarbonato",
        "bestsellers_h2": "Los 3 modelos con techo de policarbonato disponibles",
        "beneficios_h2": "Techo de policarbonato: luz natural, 15+ años de vida. INIFED.",
        "faq_h2": "Preguntas frecuentes · Gradas con techo de policarbonato",
        "faq1_q": "¿Por qué el techo de policarbonato es el único INIFED?",
        "faq1_a": "El Instituto Nacional de la Infraestructura Física Educativa (<strong>INIFED</strong>) exige techos translúcidos que permitan luz natural y resistan granizo en infraestructura escolar pública. El policarbonato de 6mm cumple ambos requisitos: deja pasar el 80% de luz visible y soporta impactos de granizo grueso. Por eso el <strong>modelo Grada 50 Personas Techo Curvo de Policarbonato</strong> es el único modelo Sportmaster homologado para canchas escolares públicas dentro del programa La Escuela Es Nuestra (LEEN).",
        "alt_kw": "Gradas techadas con techo de policarbonato",
    },
    {
        "slug": "gradas-escolares-secundaria-prepa",
        "title": "Gradas Escolares para Secundaria y Prepa | INIFED · Sportmaster",
        "desc": "Gradas escolares para secundaria, preparatoria y colegio: modelos INIFED y opciones modulares. Acero estructural, instalación en menos de una semana. Cotiza por WhatsApp.",
        "kw": "gradas escolares, gradas para escuela, gradas para secundaria, gradas para preparatoria, gradas para colegio, gradas INIFED escolares, gradas escolares precio, gradas escuela publica, gradas con LEEN, gradas con CEAP, gradas con FAEB",
        "og_t": "Gradas Escolares · Secundaria, Prepa y Colegio · Sportmaster",
        "og_d": "Gradas para secundaria, preparatoria y colegio. Modelos INIFED para escuela pública. Instalación rápida + garantía 1 año.",
        "tw_t": "Gradas Escolares · INIFED y Modulares | Sportmaster",
        "tw_d": "Gradas para secundaria, prepa y colegio. INIFED. Cotiza por WhatsApp.",
        "bread": "Gradas Escolares para Secundaria y Prepa",
        "eyebrow": "Para escuelas · secundarias y prepas · INIFED",
        "h1_pre": "Gradas para<br>",
        "h1_acento": "escuelas",
        "h1_post": "<br>en México.",
        "sub": "Gradas para secundaria, preparatoria, colegio y planteles universitarios. Modelo <strong>INIFED</strong> oficial para escuela pública, opciones modulares para colegios privados. Instalación en menos de una semana.<br><br>Cotización en 1 a 2 horas por WhatsApp.",
        "wa_msg": "Hola!%20Soy%20de%20una%20escuela%20y%20quiero%20cotizar%20gradas%20-%20vengo%20de%20gradasdefutbol.mx",
        "bestsellers_eyebrow": "Más usadas en escuelas",
        "bestsellers_h2": "Los 3 modelos más usados en secundarias y prepas",
        "beneficios_h2": "Gradas para escuelas que aguantan generación tras generación.",
        "faq_h2": "Preguntas frecuentes · Gradas escolares",
        "faq1_q": "¿Qué gradas escolares pueden comprar las escuelas públicas con LEEN, CEAP o FAEB?",
        "faq1_a": "Las escuelas públicas (secundarias y primarias) pueden adquirir el <strong>modelo Grada 50 Personas Techo Curvo de Policarbonato INIFED</strong> con recurso de los programas La Escuela Es Nuestra (LEEN), CEAP o FAEB. Es el único modelo Sportmaster homologado por el Instituto Nacional de la Infraestructura Física Educativa. Las preparatorias, colegios privados y planteles universitarios pueden optar por cualquiera de los 12 modelos según presupuesto y capacidad requerida.",
        "alt_kw": "Gradas escolares secundaria y prepa",
    },
    {
        "slug": "gradas-de-acero-estructural",
        "title": "Gradas de Acero Estructural para Canchas Deportivas | Sportmaster",
        "desc": "Gradas de acero estructural con tratamiento anticorrosivo: 12 modelos para canchas deportivas. Soldaduras certificadas, 35 a 150 personas. Garantía 1 año. Cotiza por WhatsApp.",
        "kw": "gradas de acero, gradas acero estructural, gradas de metal, gradas de hierro, gradas metalicas acero, gradas para canchas acero, gradas industriales acero, gradas modulares acero, fabricante gradas acero mexico",
        "og_t": "Gradas de Acero Estructural · 12 Modelos | Sportmaster México",
        "og_d": "Gradas de acero estructural con tratamiento anticorrosivo. 12 modelos para fútbol, pádel y escuela. Soldaduras certificadas.",
        "tw_t": "Gradas de Acero Estructural para Canchas | Sportmaster",
        "tw_d": "Gradas de acero con tratamiento anticorrosivo. 12 modelos. Cotiza por WhatsApp.",
        "bread": "Gradas de Acero Estructural",
        "eyebrow": "Acero estructural · soldaduras certificadas · MX",
        "h1_pre": "Gradas de<br>",
        "h1_acento": "acero estructural",
        "h1_post": "<br>para canchas.",
        "sub": "12 modelos en acero estructural calibre 14 con tratamiento anticorrosivo completo. Soldaduras certificadas, capacidad de <strong>35 a 150 personas</strong>. Diseñadas para uso intensivo en exterior por más de 15 años.<br><br>Cotización en 1 a 2 horas por WhatsApp.",
        "wa_msg": "Hola!%20Quiero%20cotizar%20gradas%20de%20acero%20estructural%20-%20vengo%20de%20gradasdefutbol.mx",
        "bestsellers_eyebrow": "En acero estructural",
        "bestsellers_h2": "Los 3 modelos en acero estructural más vendidos",
        "beneficios_h2": "Acero estructural con tratamiento anticorrosivo. Sin letra pequeña.",
        "faq_h2": "Preguntas frecuentes · Gradas de acero estructural",
        "faq1_q": "¿Qué calibre y tipo de acero usan en las gradas Sportmaster?",
        "faq1_a": "Usamos <strong>acero estructural calibre 14</strong> con tratamiento anticorrosivo completo en toda la estructura: limpieza con chorro de arena, primer epóxico y pintura de esmalte horneable. Las soldaduras están certificadas bajo norma. La estructura resiste cargas dinámicas de uso intensivo en exteriores y tiene vida útil de más de 15 años en condiciones normales de operación. Para zonas costeras o climas con alta humedad, agregamos doble capa de protección anticorrosiva.",
        "alt_kw": "Gradas de acero estructural",
    },
    {
        "slug": "tribunas-metalicas-para-canchas",
        "title": "Tribunas Metálicas para Canchas Deportivas | 12 Modelos | Sportmaster",
        "desc": "Tribunas metálicas para canchas deportivas: 12 modelos con techo. Capacidad 35 a 150 personas. Acero estructural anticorrosivo. INIFED. Cotiza por WhatsApp.",
        "kw": "tribunas metalicas, tribunas para canchas, tribunas para canchas de futbol, tribunas para canchas deportivas, tribunas con techo, tribunas metalicas precio, tribunas modulares, fabricante tribunas mexico, tribunas para estadios pequeños",
        "og_t": "Tribunas Metálicas para Canchas Deportivas · México",
        "og_d": "Tribunas metálicas con techo para canchas deportivas. 12 modelos, 35 a 150 personas. Acero estructural. INIFED.",
        "tw_t": "Tribunas Metálicas para Canchas | Sportmaster",
        "tw_d": "Tribunas metálicas con techo · 12 modelos · INIFED. Cotiza por WhatsApp.",
        "bread": "Tribunas Metálicas para Canchas",
        "eyebrow": "Tribunas con techo · 12 modelos · INIFED",
        "h1_pre": "Tribunas<br>",
        "h1_acento": "metálicas",
        "h1_post": "<br>para canchas.",
        "sub": "Fabricamos tribunas metálicas con techo para canchas deportivas: <strong>fútbol 7, pádel, club, hotel y municipio</strong>. 12 modelos en acero estructural, capacidad de 35 a 150 personas.<br><br>Cotización en 1 a 2 horas por WhatsApp.",
        "wa_msg": "Hola!%20Quiero%20cotizar%20tribunas%20metalicas%20para%20mi%20cancha%20-%20vengo%20de%20gradasdefutbol.mx",
        "bestsellers_eyebrow": "Top tribunas",
        "bestsellers_h2": "Las 3 tribunas metálicas más vendidas",
        "beneficios_h2": "Tribunas metálicas que aguantan público en pie. Sin letra pequeña.",
        "faq_h2": "Preguntas frecuentes · Tribunas metálicas",
        "faq1_q": "¿Cuál es la diferencia entre gradas y tribunas?",
        "faq1_a": "Para fines comerciales los términos son <strong>sinónimos</strong> en México. \"Grada\" y \"tribuna\" se refieren a la misma estructura metálica de bancas escalonadas para canchas deportivas. Algunos arquitectos llaman \"tribuna\" a estructuras de mayor capacidad (100 personas o más) y \"grada\" a estructuras menores, pero técnicamente son el mismo producto. Sportmaster fabrica 12 modelos que se ajustan a cualquier necesidad: desde tribunas móviles de 12 asientos hasta tribunas fijas de 150 personas.",
        "alt_kw": "Tribunas metálicas para canchas deportivas",
    },
    {
        "slug": "venta-gradas-metalicas-mexico",
        "title": "Venta de Gradas Metálicas en México | Fábrica Directa | Sportmaster",
        "desc": "Venta directa de fábrica de gradas metálicas en México: 12 modelos con precio real, sin intermediarios. Envío a 32 estados. Cotiza por WhatsApp en 1 a 2 horas.",
        "kw": "venta de gradas metalicas, comprar gradas metalicas, venta gradas deportivas mexico, gradas metalicas fabrica directa, gradas metalicas en venta, gradas para vender, fabricante gradas mexico, cotizacion gradas metalicas, gradas metalicas mayoreo",
        "og_t": "Venta de Gradas Metálicas · Fábrica Directa México",
        "og_d": "Venta directa de fábrica de gradas metálicas. 12 modelos, sin intermediarios. Envío a 32 estados. INIFED.",
        "tw_t": "Venta Gradas Metálicas Fábrica Directa | Sportmaster",
        "tw_d": "Venta de gradas metálicas directo de fábrica. 12 modelos. Sin intermediarios.",
        "bread": "Venta de Gradas Metálicas en México",
        "eyebrow": "Fábrica directa · sin intermediarios · 32 estados",
        "h1_pre": "Venta de<br>",
        "h1_acento": "gradas metálicas",
        "h1_post": "<br>en México.",
        "sub": "Compra directo de fábrica: <strong>12 modelos de gradas metálicas</strong> con precio real, sin intermediarios ni comisiones. Fabricamos en Monterrey y enviamos a los 32 estados de la República.<br><br>Cotización en 1 a 2 horas por WhatsApp.",
        "wa_msg": "Hola!%20Quiero%20comprar%20gradas%20metalicas%20-%20vengo%20de%20gradasdefutbol.mx",
        "bestsellers_eyebrow": "Top venta",
        "bestsellers_h2": "Los 3 modelos más vendidos directo de fábrica",
        "beneficios_h2": "Compra de fábrica: precio real, sin intermediarios. Sin letra pequeña.",
        "faq_h2": "Preguntas frecuentes · Venta de gradas metálicas",
        "faq1_q": "¿Cómo se compra una grada metálica directo de fábrica Sportmaster?",
        "faq1_a": "El proceso es: <strong>(1)</strong> envíanos por WhatsApp el modelo que te interesa, capacidad, ciudad y fecha estimada de instalación. <strong>(2)</strong> Respondemos cotización formal en 1 a 2 horas con precio + IVA, ficha técnica PDF, tiempo de fabricación y costo de flete a tu ciudad. <strong>(3)</strong> Confirmas con 50% de anticipo. <strong>(4)</strong> Fabricamos en 4 a 6 semanas. <strong>(5)</strong> Enviamos a tu ciudad y coordinamos la instalación. No tenemos distribuidores ni intermediarios: la venta es siempre directa de fábrica Sportmaster.",
        "alt_kw": "Venta de gradas metálicas",
    },
]

# ALT base del template (sin "Gradas para canchas deportivas" — esa salió del spoke 1)
# Para cada spoke replazamos las ALT del template precio (que dicen "Grada deportiva 35 personas..." etc)
ALT_TEMPLATES = [
    ("Grada de fútbol metálica con techo de lona 75 personas para cancha de club semiprofesional",
     "{kw} 75 personas techo curvo lona club semiprofesional"),
    ("Grada de fútbol metálica con techo de policarbonato 50 personas INIFED para escuela pública",
     "{kw} 50 personas INIFED policarbonato escuela pública"),
    ("Grada de fútbol metálica para estadio 150 personas techo curvo de lona Sportmaster México",
     "{kw} 150 personas techo curvo lona estadio Sportmaster"),
    ("Grada deportiva 35 personas techo curvo de lona", "{kw} 35 personas techo curvo lona"),
    ("Grada deportiva 35 personas techo curvo policarbonato", "{kw} 35 personas techo curvo policarbonato"),
    ("Grada deportiva 50 personas techo curvo lona", "{kw} 50 personas techo curvo lona"),
    ("Grada 50 personas INIFED policarbonato", "{kw} 50p INIFED policarbonato"),
    ("Grada 75 personas techo curvo lona", "{kw} 75p techo curvo lona"),
    ("Grada 75 personas policarbonato", "{kw} 75p techo policarbonato"),
    ("Grada 100 personas techo recto lona", "{kw} 100p techo recto lona"),
    ("Grada metálica para exteriores 150 personas techo curvo lámina galvanizada para estadio de fútbol",
     "{kw} 150p techo lámina galvanizada estadio exteriores"),
    ("Grada Flex 35 personas techo lona", "{kw} Flex 35p techo lona desmontable"),
    ("Grada Flex 35 personas policarbonato", "{kw} Flex 35p techo policarbonato desmontable"),
    ("Gradas móviles 12 asientos con ruedas para pádel y eventos", "{kw} móviles 12 asientos pádel y eventos"),
    ("Gradas móviles 12 asientos con ruedas", "{kw} móviles 12 asientos con ruedas"),
]


INTERNAL_LINKS_TMPL = '<p style="margin-top:1rem;color:var(--texto-suave);font-size:.95rem">Ver también: <a href="/precio-gradas-metalicas-mexico-2026/" style="color:var(--lime);text-decoration:underline">precios de los 12 modelos</a> · <a href="/medidas-gradas-deportivas/" style="color:var(--lime);text-decoration:underline">medidas y dimensiones</a> · <a href="/" style="color:var(--lime);text-decoration:underline">home Sportmaster Gradas</a></p>'


def transform(s, sp):
    # META SEO
    s = re.sub(r'<title>[^<]+</title>', f'<title>{sp["title"]}</title>', s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]+"', f'<meta name="description" content="{sp["desc"]}"', s, count=1)
    s = re.sub(r'<meta name="keywords" content="[^"]+"', f'<meta name="keywords" content="{sp["kw"]}"', s, count=1)
    s = re.sub(r'<link rel="canonical" href="[^"]+"', f'<link rel="canonical" href="https://gradasdefutbol.mx/{sp["slug"]}/"', s, count=1)
    s = re.sub(r'<meta property="og:title" content="[^"]+"', f'<meta property="og:title" content="{sp["og_t"]}"', s, count=1)
    s = re.sub(r'<meta property="og:description" content="[^"]+"', f'<meta property="og:description" content="{sp["og_d"]}"', s, count=1)
    s = re.sub(r'<meta property="og:url" content="[^"]+"', f'<meta property="og:url" content="https://gradasdefutbol.mx/{sp["slug"]}/"', s, count=1)
    s = re.sub(r'<meta name="twitter:title" content="[^"]+"', f'<meta name="twitter:title" content="{sp["tw_t"]}"', s, count=1)
    s = re.sub(r'<meta name="twitter:description" content="[^"]+"', f'<meta name="twitter:description" content="{sp["tw_d"]}"', s, count=1)

    # Breadcrumb schema
    s = re.sub(
        r'\{"@type":"ListItem","position":2,"name":"[^"]+","item":"https://gradasdefutbol\.mx/[^"]+"\}',
        f'{{"@type":"ListItem","position":2,"name":"{sp["bread"]}","item":"https://gradasdefutbol.mx/{sp["slug"]}/"}}',
        s, count=1
    )

    # HERO
    s = re.sub(r'<div class="hero-v2-eyebrow">[^<]+</div>', f'<div class="hero-v2-eyebrow">{sp["eyebrow"]}</div>', s, count=1)
    s = re.sub(r'<h1 class="hero-v2-headline">.*?</h1>',
               f'<h1 class="hero-v2-headline">{sp["h1_pre"]}<span class="acento">{sp["h1_acento"]}</span>{sp["h1_post"]}</h1>',
               s, count=1, flags=re.DOTALL)
    s = re.sub(r'<p class="hero-v2-sub">.*?</p>',
               f'<p class="hero-v2-sub">{sp["sub"]}</p>',
               s, count=1, flags=re.DOTALL)
    s = re.sub(r'Hola!%20Quiero%20cotizar%20una%20grada[^"]+', sp["wa_msg"], s, count=1)

    # Bestsellers eyebrow + h2
    s = re.sub(r'<div class="section-eyebrow">Top precio-valor 2026</div>',
               f'<div class="section-eyebrow">{sp["bestsellers_eyebrow"]}</div>', s, count=1)
    s = re.sub(r'<h2 class="section-title">Los 3 modelos con mejor precio-valor del catálogo</h2>',
               f'<h2 class="section-title">{sp["bestsellers_h2"]}</h2>', s, count=1)

    # Beneficios h2
    s = re.sub(r'<h2 class="section-title">Gradas metálicas con garantía y acero estructural\. Sin letra pequeña\.</h2>',
               f'<h2 class="section-title">{sp["beneficios_h2"]}</h2>', s, count=1)

    # FAQ h2 + internal links
    s = re.sub(r'<h2 class="section-title">Todo lo que necesitas saber antes de cotizar</h2>',
               f'<h2 class="section-title">{sp["faq_h2"]}</h2>{INTERNAL_LINKS_TMPL}', s, count=1)

    # FAQ #1 schema (replaces ¿Cuál es el precio...)
    s = s.replace(
        '{"@type":"Question","name":"¿Cuál es el precio de una grada metálica en México 2026?","acceptedAnswer":{"@type":"Answer","text":"En 2026 los precios reales de gradas metálicas Sportmaster van desde $49,500 MXN (Grada Móvil 12 Asientos) hasta $245,000 MXN (Grada 150 Personas con techo curvo). Una grada de 35 personas con techo arranca en $78,000 MXN, la de 50 personas en $99,500 MXN (INIFED en $105,000), la de 75 personas en $118,000 MXN y la de 100 personas en $138,000 MXN. Todos los precios son + IVA, no incluyen flete ni instalación."}}',
        '{"@type":"Question","name":"' + sp["faq1_q"] + '","acceptedAnswer":{"@type":"Answer","text":"' + re.sub(r'<[^>]+>', '', sp["faq1_a"]) + '"}}'
    )

    # FAQ #1 visible (replaces ¿Cuánto cuesta una grada deportiva?)
    s = s.replace(
        '<details><summary>¿Cuánto cuesta una grada deportiva?</summary><p>Los precios van desde <strong>$49,500 MXN</strong> para gradas móviles de 12 asientos hasta <strong>$245,000 MXN</strong> para gradas de 150 personas. Todos los precios son <strong>más IVA</strong> y <strong>no incluyen flete ni instalación</strong>. Solicita una cotización formal para tu ciudad.</p></details>',
        f'<details><summary>{sp["faq1_q"]}</summary><p>{sp["faq1_a"]}</p></details>'
    )

    # ALT
    for old, tmpl in ALT_TEMPLATES:
        new = tmpl.format(kw=sp["alt_kw"])
        s = s.replace(f'alt="{old}', f'alt="{new}')

    return s


def main():
    src = open(SRC).read()
    for sp in SPOKES:
        out_dir = f"{ROOT}/{sp['slug']}"
        os.makedirs(out_dir, exist_ok=True)
        out = transform(src, sp)
        with open(f"{out_dir}/index.html", "w") as f:
            f.write(out)
        print(f"  ✓ /{sp['slug']}/")
    print(f"\n✓ {len(SPOKES)} spokes generados.")


if __name__ == "__main__":
    main()
