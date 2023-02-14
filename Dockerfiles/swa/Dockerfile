FROM nginx:stable-alpine
ADD nginx.conf /etc/nginx
WORKDIR /usr/share/nginx/html
RUN rm -rf ./* 
ADD TMP_OUT  ./
COPY .env ./
RUN apk add vim
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
