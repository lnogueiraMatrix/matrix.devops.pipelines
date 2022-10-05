FROM nginx:stable-alpine
ADD nginx.conf /etc/nginx
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
ADD TMP_OUT/*  ./
CMD [ "nginx", "-g", "daemon off;" ]