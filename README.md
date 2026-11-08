# Dislate Producciones — dislateproducciones.com

Web estática de Dislate Producciones SL (línea editorial: logotipo grande, tipografía mezclada e índice de proyectos).

- Datos editables desde el Gestor de webs del portal de Grupo Livon (o a mano): `data/proyectos.json`, `data/servicios.json`, `data/portada.json`.
- `scripts/generar.py` crea las páginas; la acción de GitHub lo ejecuta al cambiar los datos. No edites los `.html` a mano.
- Se publica en el servidor propio (Coolify, OVH) con `Dockerfile` + `nginx.conf`, no en Cloudflare, para evitar los bloqueos de IPs de LaLiga.
