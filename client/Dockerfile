# build stage
# todo - check mherman vue blog post on dcker
FROM node:14-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY default.conf /etc/nginx/conf.d/
COPY --from=build-stage /app/dist/ /usr/share/nginx/html/
CMD sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'