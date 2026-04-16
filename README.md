# Sportmaster — Gradas Deportivas INIFED

Sitio premium optimizado para SEO, AEO y conversión. Rebuild completo del subdominio `gradas-deportivas-futbol.sportmaster.mx` con enfoque en **gradas INIFED con memoria de cálculo firmada**.

## Stack

- **HTML5 + Tailwind CSS** (CDN, sin build)
- **Vanilla JS** (count-up animations + filter chips Apple-style)
- **SEO/AEO**: 8 schemas JSON-LD, sitemap, robots, llms.txt, OG completo
- **Performance**: lazy loading, font preload, hero con fetchpriority high
- **Responsive**: mobile-first, breakpoints 640/768/1024/1280 con text-scaling y filter chips scrollable en móvil

## Estructura

```
.
├── index.html                                        → Landing principal (INIFED + catálogo)
├── sitemap.xml                                       → 10 URLs (landing + blog)
├── robots.txt                                        → Allow all + sitemap
├── llms.txt                                          → Resumen para AI crawlers
├── assets/
│   ├── logo_sportmaster.webp                         → (copiar del sitio original)
│   └── img/
│       └── grada-inifed-50p.png                      → Render INIFED 50 espectadores
├── docs/
│   └── ficha-tecnica-grada-inifed-50-personas.pdf    → Ficha técnica oficial
├── blog/
│   ├── index.html                                    → Blog landing
│   ├── gradas-inifed-normativa-que-cumplen/          → Art 1: Normativa (10 min)
│   │   └── index.html
│   ├── como-elegir-capacidad-grada-cancha-futbol/    → Art 2: Guía capacidad (8 min)
│   │   └── index.html
│   └── gradas-inifed-planos-que-incluyen/            → Art 3: Planos y memoria (12 min)
│       └── index.html
└── README.md
```

## Cambios v2 (este build)

1. **Filtro Apple-style** en catálogo con chips segmentados horizontales y transición fluida al filtrar tarjetas (filtra por capacidad: Todas / 12 / 35 / 50 / 75 / 100 / 150 / INIFED)
2. **Facturación SAT analizada**: mantenida pero consolidada en un solo badge institucional (con órdenes de compra gobierno), removida del trust strip superior para no saturar
3. **Banner intermedio reemplazado**: ya no pide plano; nuevo mensaje "Gradas INIFED listas en 20 días. Sin espera, sin sorpresas" enfocado en modelos estandarizados
4. **Opción personalizada reducida**: enfoque en modelos estándar, no se pide plano en ningún CTA
5. **Blog independiente** en `/blog/` con 3 artículos iniciales SEO/AEO optimizados (Article + FAQPage + Breadcrumb schemas)
6. **Timing actualizado**: 15 días fabricación + 5 días instalación = **20 días total** (antes 30)
7. **Fotos originales** del sitio Sportmaster referenciadas vía CDN directo (se cargan en navegador del usuario, no en este container)
8. **Mobile responsive verificado**: text scaling clamp, filter chips con scroll-x en móvil, grid colapsa 3→2→1 columnas, hero reduce tipografía en pantallas pequeñas
9. **Keywords INIFED**: "gradas inifed", "gradas inifed planos", "gradas deportivas inifed" integradas en Title, Meta, H1, H2, párrafos, alt text, schemas y FAQ
10. **Nueva grada INIFED 50 espectadores** añadida como sección hero dedicada + primera card del catálogo + en blog + en schemas (Product schema completo con todas las propiedades técnicas)

## Deploy local

```bash
npx serve .
# o
python3 -m http.server 8080
```

## Deploy a Cloudflare Pages

### Opción A — Git (recomendada)

```bash
# Si tienes GitHub CLI
gh repo create gradas-sportmaster --public --source=. --remote=origin --push

# O manualmente en https://github.com/new, luego:
git init
git add .
git commit -m "feat: rebuild premium v2 with INIFED + blog"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/gradas-sportmaster.git
git push -u origin main
```

En Cloudflare → Pages → Create → Connect to Git → elegir repo → build config:
- Framework preset: None
- Build command: (vacío)
- Build output directory: `/`

### Opción B — Wrangler CLI

```bash
npm install -g wrangler
wrangler login
wrangler pages deploy . --project-name=gradas-sportmaster
```

### Dominio custom

En Cloudflare Pages → Custom domains → Add → `gradas-deportivas-futbol.sportmaster.mx`

## Checklist post-deploy

- [ ] HTTPS funciona
- [ ] `sitemap.xml` accesible
- [ ] `llms.txt` accesible
- [ ] `/blog/` accesible con los 3 artículos
- [ ] `/docs/ficha-tecnica-grada-inifed-50-personas.pdf` accesible
- [ ] Schemas validan en https://validator.schema.org/
- [ ] PageSpeed > 90 móvil
- [ ] Google Search Console: propiedad + sitemap
- [ ] GA4 / Meta Pixel insertados (si aplica)

## Imágenes pendientes de subir

Las fotos de producto están referenciadas vía CDN del sitio actual:
`https://gradas-deportivas-futbol.sportmaster.mx/assets/img/...`

Funcionan en navegador inmediatamente. Para producción óptima, copiar también a `/assets/img/` local para no depender del CDN externo:

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
- `logo_sportmaster.webp`

La imagen INIFED (`grada-inifed-50p.png`) y el PDF (`ficha-tecnica-grada-inifed-50-personas.pdf`) ya están incluidos.

## Próximas iteraciones recomendadas

- Generar páginas individuales por modelo (`/modelos/grada-75-personas/`) con schema Product dedicado por cada una
- Añadir casos reales con 6 proyectos entregados (fotos + nombre de cliente + ciudad)
- 4 artículos de blog adicionales (1 por mes) para mantener posicionamiento AEO
- Integrar formulario de contacto backend (Formspree, Netlify Forms o n8n)
- A/B test headline del hero entre "Entrega en 20 días" vs "Memoria de cálculo firmada"
