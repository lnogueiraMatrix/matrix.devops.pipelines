ARG DESTINATION=./dist
FROM nginx:stable-alpine
ADD nginx.conf /etc/nginx

WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
ADD ${DESTINATION}/*  ./
CMD [ "nginx", "-g", "daemon off;" ]