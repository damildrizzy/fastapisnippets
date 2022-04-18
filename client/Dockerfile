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
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
RUN sudo chown -R www-data:www-data /var/log/nginx;
RUN sudo chmod -R 755 /var/log/nginx;
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]