FROM public.ecr.aws/docker/library/python:3.11.4-alpine3.17
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
# Python deps
RUN mkdir /web
WORKDIR /web
COPY docker/requirements.txt /web/
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
COPY ./web /web/
RUN ["chmod", "+x", "/web/scripts/prod/docker-entrypoint.sh"]
ENTRYPOINT ["/web/scripts/prod/docker-entrypoint.sh"]
