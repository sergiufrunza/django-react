FROM public.ecr.aws/docker/library/python:3.11.4-alpine3.17
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
# Python deps
RUN mkdir /backend
WORKDIR /backend
COPY docker/requirements.txt /backend/
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
COPY ./backend /backend/
RUN ["chmod", "+x", "/backend/scripts/prod/docker-entrypoint.sh"]
ENTRYPOINT ["/backend/scripts/prod/docker-entrypoint.sh"]
