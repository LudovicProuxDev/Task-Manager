# Utilisation d'une image Nginx stable basée sur Alpine pour la légèreté
FROM nginx:stable-alpine

# Suppression de la configuration par défaut de Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copie la configuration Nginx (qui est maintenant à la racine du contexte)
COPY nginx.conf /etc/nginx/conf.d/

# Copie tous les fichiers statiques du dossier actuel vers Nginx
COPY . /usr/share/nginx/html/

# Sécurité : On change les permissions pour permettre à un utilisateur non-root
# de manipuler les dossiers temporaires de Nginx
RUN touch /var/run/nginx.pid && \
    chown -R nginx:nginx /var/run/nginx.pid /var/cache/nginx /var/log/nginx /etc/nginx/conf.d

# On passe à l'utilisateur 'nginx' défini dans l'image de base
USER nginx

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
