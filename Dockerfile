# Web estática servida con nginx: imagen para Coolify (servidor OVH de Grupo Livon).
# Se sirve desde el servidor propio y no desde Cloudflare para evitar los bloqueos de IPs de LaLiga.
FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY . /usr/share/nginx/html
EXPOSE 80
