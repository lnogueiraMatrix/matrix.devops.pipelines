FROM nginx:stable-alpine
COPY nginx.conf /etc/nginx
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY TMP_OUT/  ./
CMD [ "nginx", "-g", "daemon off;" ]