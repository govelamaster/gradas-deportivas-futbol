# CLAUDE.md — Sportmaster Gradas Deportivas

## Project
Landing premium + blog SEO/AEO para Sportmaster Gradas Deportivas.
Producción: https://gradasdefutbol.mx (Cloudflare Worker auto-deploy desde main).

## Stack
- HTML/CSS vanilla (sin framework, Inter font de Google Fonts)
- Hosted: Cloudflare Workers (auto-deploy on push to main)
- DNS + Registrar: Cloudflare
- Repo: github.com/govelamaster/gradas-deportivas-futbol

## Brand guidelines
- Verde primary: #1B5E20
- Verde dark: #0D3510
- Naranja CTA: #F57C00
- Font: Inter (400-900) desde Google Fonts
- Logo: SPORT (verde) + MASTER (naranja)
- WhatsApp: +52 1 81 1629 6384 (wa.me/5218116296384)
- Email corporativo: info@sportmaster.com.mx

## Business rules (NO NEGOCIABLES)
- Precios siempre con leyenda "+ IVA · No incluye flete ni instalación"
- Sólo el modelo Grada 50P Policarbonato 6mm cumple INIFED (ningún otro modelo puede decir "INIFED")
- Nunca mencionar TenCate, Mattex, Shaw, Bonar como proveedores
- Pasto sintético nunca se describe como "europeo", usar "importado de alto rendimiento"
- PadelCenter no hace bases, pickleball usa pintura en concreto (no turf)
- Response time promise: "menos de 1 hora" por WhatsApp
- No prometer visitas ni mediciones en sitio

## Catálogo vigente (12 modelos con precios reales MXN + IVA)
| Modelo | Cap | Precio |
|---|---|---|
| Grada 35P Techo Curvo Lona | 35 | $78,000 |
| Grada 35P Techo Curvo Policarbonato | 35 | $88,000 |
| Grada 50P Techo Curvo Lona | 50 | $99,500 |
| Grada 50P Techo Curvo Policarbonato (INIFED) | 50 | $105,000 |
| Grada 75P Techo Curvo Lona | 75 | $118,000 |
| Grada 75P Techo Curvo Policarbonato | 75 | $135,000 |
| Grada 100P Techo Recto Lona | 100 | $138,000 |
| Grada 150P Techo Curvo Lona | 150 | $245,000 |
| Grada 150P Techo Curvo Lámina Galvanizada | 150 | $245,000 |
| Grada Flex 35P Techo Lona | 35 | $78,000 |
| Grada Flex 35P Techo Policarbonato | 35 | $88,000 |
| Gradas Móviles 12 Asientos con Ruedas | 12 | $49,500 |

## Structure
- /index.html — landing principal (hero, catálogo 12 modelos, INIFED, FAQ)
- /blog/ — 3 artículos SEO/AEO (normativa INIFED, capacidad, planos)
- /docs/ — 12 fichas técnicas PDF (una por modelo)
- /assets/img/ — fotos productos
- /sitemap.xml, /robots.txt, /llms.txt

## SEO keywords primarias
- gradas deportivas, gradas para cancha de futbol, gradas metálicas
- gradas INIFED, gradas prefabricadas, tribunas deportivas
- gradas techadas México, venta de gradas
- gradas con techo de policarbonato, gradas con techo de lona

## Workflow on changes
Cuando se pida un cambio:
1. Editar archivo(s) relevante(s) manteniendo brand guidelines y business rules
2. Si afecta sitemap (URLs nuevas/eliminadas), actualizar sitemap.xml con <lastmod> de hoy
3. Si afecta datos de modelo (precio, spec), actualizar:
   - index.html (tarjeta + schema JSON-LD ItemList)
   - llms.txt (tabla de catálogo)
   - docs/grada-<slug>.pdf (regenerar con reportlab si existe el script)
4. git add -A && git commit con mensaje descriptivo en inglés
5. git push origin main
6. Cloudflare redeploya solo en ~60s
7. Confirmar al usuario con URL de verificación

## Execution mode (critical)
- NO narrar proceso, NO recapitular requests, NO thinking out loud
- Ejecutar directo y entregar sólo el resultado final útil
- Código = diff exacto o bloque
- Mínimos tokens, máxima densidad

## Style rules
- No gráficos en presentaciones de cash flow (solo texto)
- Premium, bold, aspiracional; no cheesy
- Nunca "lidero" para self-description
- Mexican voice cálido, no corporativo gringo
