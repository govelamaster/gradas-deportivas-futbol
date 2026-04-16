# Sportmaster — Gradas Deportivas

Sitio premium optimizado para SEO, AEO y conversión. Rebuild completo del subdominio `gradas-deportivas-futbol.sportmaster.mx`. El modelo INIFED está posicionado como vertical especializado, sin comprometer afirmaciones sobre el resto del catálogo.

## Stack

- **HTML5 + Tailwind CSS** (CDN, sin build)
- **Vanilla JS** (count-up animations + filter chips Apple-style)
- **SEO/AEO**: 8 schemas JSON-LD, sitemap, robots, llms.txt, OG completo
- **Performance**: lazy loading, font preload, hero con fetchpriority high
- **Responsive**: mobile-first, breakpoints 640/768/1024/1280

## Estructura

```
.
├── index.html                                        → Landing principal
├── sitemap.xml                                       → 10 URLs (landing + blog)
├── robots.txt                                        → Allow all + sitemap
├── llms.txt                                          → Resumen para AI crawlers
├── assets/
│   ├── logo_sportmaster.webp                         → Logo (copiar del sitio actual)
│   └── img/
│       └── grada-inifed-50p.png                      → Render INIFED 50 espectadores
├── docs/
│   └── ficha-tecnica-grada-inifed-50-personas.pdf    → Ficha técnica oficial
├── blog/
│   ├── index.html                                    → Blog landing
│   ├── gradas-inifed-normativa-que-cumplen/
│   ├── como-elegir-capacidad-grada-cancha-futbol/
│   └── gradas-inifed-planos-que-incluyen/
└── README.md
```

## Changelog

### v3 (este build)
1. **Hero más claro**: imagen pasa de `opacity-40` a `opacity-75`, nuevo gradient lateral suave que solo oscurece el lado izquierdo (texto) y deja visible la foto. Añadido `text-shadow` al subtítulo para legibilidad sin competir con la imagen.
2. **INIFED solo en el modelo 50p**: removidas todas las afirmaciones genéricas de "gradas INIFED" del sitio. El modelo INIFED ahora tiene una sección dedicada con header explícito: *"Único modelo con cumplimiento INIFED"* + subtítulo que aclara *"El resto de nuestro catálogo son modelos comerciales estándar"*.
3. **Title, Meta, H1, Nav, Trust strip, CTAs, Footer, WhatsApp links** todos limpios de menciones genéricas de INIFED.
4. **Schemas JSON-LD corregidos**: LocalBusiness name, Service serviceType, OfferCatalog name, BreadcrumbList y FAQPage ahora son neutros. El único lugar donde aparece INIFED es en el schema `Product` específico del modelo 50p.
5. **FAQ reformulado**: la pregunta "¿Todas las gradas Sportmaster cumplen INIFED?" tiene respuesta explícita "No. Solo nuestro modelo de 50 espectadores con policarbonato 6mm".
6. **Comparativa actualizada**: fila "Cumple INIFED" (afirmativa para metal) reemplazada por "Factura SAT" (más útil y honesta).
7. **Blog alineado**: artículo 2 ya no promete "grada INIFED de 100 personas", aclara que el modelo INIFED solo existe en 50p. Artículo 1 CTA específico del modelo.
8. **llms.txt reescrito**: sección "Importante sobre INIFED" explícita sobre qué modelo cumple.

### v2
- Filtro chips Apple-style en catálogo
- Facturación SAT consolidada en un solo badge institucional
- Banner intermedio sin pedir planos
- Blog independiente con 3 artículos iniciales SEO/AEO
- Timing 15+5 = 20 días
- Fotos originales integradas desde CDN
- Grada INIFED 50 espectadores añadida

### v1
- Rebuild inicial con schemas, proceso, cobertura, garantía, FAQ
- Trust bar con 4 KPIs count-up
- Tabla comparativa metal vs concreto vs aluminio

## Deploy local

```bash
npx serve .
# o
python3 -m http.server 8080
```

## Deploy a Cloudflare Pages

```bash
# GitHub
gh repo create gradas-sportmaster --public --source=. --remote=origin --push

# O manualmente
git remote add origin https://github.com/TU_USUARIO/gradas-sportmaster.git
git push -u origin main

# Cloudflare Wrangler
npm install -g wrangler
wrangler login
wrangler pages deploy . --project-name=gradas-sportmaster
```

Luego en Cloudflare Pages → Custom domains → `gradas-deportivas-futbol.sportmaster.mx`

## Checklist post-deploy

- [ ] HTTPS funciona
- [ ] `sitemap.xml` accesible
- [ ] `llms.txt` accesible
- [ ] `/blog/` y los 3 artículos accesibles
- [ ] `/docs/ficha-tecnica-grada-inifed-50-personas.pdf` accesible
- [ ] Schemas validan en https://validator.schema.org/
- [ ] PageSpeed > 90 móvil
- [ ] Google Search Console: propiedad + sitemap
- [ ] GA4 / Meta Pixel insertados

## Imágenes que debes copiar

Desde el sitio actual `https://gradas-deportivas-futbol.sportmaster.mx/assets/` copiar a `/assets/` local:

**Logo:** `logo_sportmaster.webp` y `logo_sportmaster.png`

**Productos (a `/assets/img/`):**
- `GRADA 35 P TECHO CURVO LONA.webp`
- `GRADA 35 P TECHO CURVO POLICARBONATO - copia.webp`
- `GRADA 50P TECHO CURVO LONA ROJA.webp`
- `GRADA 50 P TECHO CURVO LONA ROJA 2.webp`
- `GRADA 75 P TECHO CURVO LONA.webp`
- `GRADA 75 P TECHO CURVO LONA BLANCA.webp`
- `GRADA 75 P TECHO CURVO LONA 2.webp`
- `GRADA 75 P TECHO CURVO LONA BLANCA 2.webp`
- `GRADA 100P TECHO RECTO LONA.webp`
- `GRADA FLEX 35P TECHO LONA.webp`
- `1 4.webp`

La imagen INIFED (`grada-inifed-50p.png`) y el PDF ya están incluidos en el zip. Durante el preview en navegador, las imágenes de productos se cargan desde el CDN del sitio actual; para deploy final copiarlas localmente.

## Posicionamiento legal/comercial

Este sitio ha sido ajustado para **no afirmar** cumplimiento INIFED en ningún modelo excepto el de 50 espectadores con policarbonato 6mm. Esto protege ante:
- Auditorías de obras con recursos públicos (SEP, "La Escuela es Nuestra", FONE)
- Licitaciones que verifiquen respaldo documental
- Clientes institucionales que comparen memoria firmada

Si en el futuro se certifica otro modelo, actualizar:
1. Nueva card en catálogo con borde lime y badge "INIFED"
2. Añadir al schema Product dentro del JSON-LD del `<head>`
3. Mencionar en sección `#inifed` como "modelo INIFED adicional"
4. Actualizar `llms.txt` en la sección "Modelos INIFED disponibles"

## Próximas iteraciones recomendadas

- Páginas individuales por modelo (`/modelos/grada-75-personas/`) con schema Product dedicado
- Sección de casos reales con 6 proyectos entregados (fotos + cliente + ciudad)
- 4 artículos de blog adicionales (1 por mes) para mantener posicionamiento AEO
- Integrar formulario backend (Formspree, Netlify Forms o n8n)
- Certificar adicionales modelos INIFED si hay demanda institucional (ampliaría catálogo elegible para licitaciones)
