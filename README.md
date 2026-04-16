# Sportmaster — Gradas Deportivas

Sitio premium optimizado para SEO, AEO y conversión. Rebuild completo del subdominio `gradas-deportivas-futbol.sportmaster.mx`.

## Stack

- **HTML5 + Tailwind CSS** (CDN, sin build)
- **Vanilla JS** (count-up animations)
- **SEO/AEO**: 7 schemas JSON-LD, sitemap, robots, llms.txt, OG completo
- **Performance**: lazy loading, font preload, hero con fetchpriority high
- **Responsive**: mobile-first, breakpoints 640/768/1024/1280

## Estructura

```
.
├── index.html         → Landing principal (todo incluido)
├── sitemap.xml        → 5 URLs con anchors
├── robots.txt         → Allow all + sitemap
├── llms.txt           → Resumen para AI crawlers
├── assets/
│   ├── logo_sportmaster.webp
│   └── img/           → Fotos de productos (copiar del sitio original)
└── README.md
```

## Deploy local

```bash
npx serve .
# o
python3 -m http.server 8080
```

## Deploy a Cloudflare Pages

### Opción A — Git (recomendada)

1. Crear repo en GitHub:
   ```bash
   gh repo create gradas-sportmaster --public --source=. --remote=origin --push
   ```
   O manualmente en https://github.com/new, luego:
   ```bash
   git init
   git add .
   git commit -m "feat: rebuild premium"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/gradas-sportmaster.git
   git push -u origin main
   ```

2. Ir a https://dash.cloudflare.com → Pages → Create → Connect to Git
3. Seleccionar el repo
4. Build config:
   - **Framework preset**: None
   - **Build command**: (vacío)
   - **Build output directory**: `/`
5. Deploy → Cloudflare asigna `gradas-sportmaster.pages.dev`

### Opción B — Wrangler CLI (deploy directo)

```bash
npm install -g wrangler
wrangler login
wrangler pages deploy . --project-name=gradas-sportmaster
```

### Dominio custom

En Cloudflare Pages → Custom domains → Add → `gradas-deportivas-futbol.sportmaster.mx`

Si el dominio ya está en Cloudflare, se configura automáticamente. Si no, apunta el CNAME del subdominio a `gradas-sportmaster.pages.dev`.

## Checklist post-deploy

- [ ] HTTPS funciona
- [ ] `sitemap.xml` accesible
- [ ] `llms.txt` accesible
- [ ] Schemas validan en https://validator.schema.org/
- [ ] PageSpeed > 90 móvil
- [ ] Google Search Console: propiedad + sitemap
- [ ] GA4 / Meta Pixel insertados (si aplica)

## Imágenes pendientes de subir

Copiar del sitio original (`https://gradas-deportivas-futbol.sportmaster.mx/assets/img/`) a `/assets/img/`:

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

Y el logo: `logo_sportmaster.webp`

Ideal: generar además `og-gradas-sportmaster.jpg` (1200×630) para Open Graph.

## Mejoras vs sitio original

| # | Antes | Después |
|---|---|---|
| 1 | "PRECIO: $0.00" en todos los productos | "Cotización personalizada" + CTA directo |
| 2 | Sin schemas JSON-LD | 7 schemas: Org, LocalBusiness, Service, Website, Breadcrumb, FAQPage, Speakable |
| 3 | Hero genérico "Gradas Deportivas Profesionales" | "600+ gradas instaladas en México. La tuya en 30 días." |
| 4 | Sin prueba social cuantitativa | Stats bar: 600+ / 17 años / 31 estados / <1h |
| 5 | Footer con links `#` | Footer navegación real + NAP + redes |
| 6 | Sin `llms.txt` | llms.txt completo en raíz |
| 7 | FAQ sin schema | 12 FAQs con FAQPage schema estructurado |
| 8 | Tipografía sistema | Archivo Black + Inter (Google Fonts) |
| 9 | Sin tabla comparativa | Metal vs Concreto vs Aluminio |
| 10 | Sin sección de cobertura | Bloque visual "31 estados" |
| 11 | Sin sección proceso | Timeline 4 pasos |

## Siguiente iteración

- Generar 6 páginas individuales por modelo (`/modelos/[slug]`) con schema Product completo por cada una
- Añadir sección de casos reales con 6 fotos de proyectos entregados
- Implementar testimonios con nombres reales
- A/B test headline hero
- Traducir versión `en-US` si se expande a US market
