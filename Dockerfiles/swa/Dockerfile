ARG DESTINATION=dist
FROM nginx:stable-alpine

COPY ./nginx.conf /etc/nginx/nginx.conf

WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY $DESTINATION  ./

CMD [ "nginx", "-g", "daemon off;" ]