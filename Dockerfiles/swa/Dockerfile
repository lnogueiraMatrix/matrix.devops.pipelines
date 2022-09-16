ARG DESTINATION=dist

FROM nginx:stable-alpine

WORKDIR /app 

COPY ./nginx.conf /etc/nginx/nginx.conf

COPY  $DESTINATION  /usr/share/nginx/html/

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=80

CMD [ "nginx", "-g", "daemon off;" ]