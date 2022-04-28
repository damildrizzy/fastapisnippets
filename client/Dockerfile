# build stage
# todo - check mherman vue blog post on dcker
FROM node:14-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN apk add --update python3 make g++\
   && rm -rf /var/cache/apk/*
RUN npm install
COPY . .
ARG VUE_APP_API_BASE_URL
ENV VUE_APP_API_BASE_URL $VUE_APP_API_BASE_URL
RUN npm run build

# production environment
FROM nginxinc/nginx-unprivileged
COPY --from=build-stage /app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d
CMD sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/nginx.conf && \
          nginx -g 'daemon off;'