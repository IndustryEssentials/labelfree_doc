# build stage
FROM python:3.9 as build-stage
WORKDIR /app
RUN pip install mkdocs-material mkdocs-glightbox -i http://mirrors.aliyun.com/pypi/simple/
COPY . /app
RUN mkdocs build --clean

# Deliver the dist folder with Nginx
FROM nginx:stable-alpine

# COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=build-stage app/site /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
