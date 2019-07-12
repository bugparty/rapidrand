FROM python:2.7-alpine
RUN apk add --no-cache cmake gcc g++ make bash \
        bash-doc \
        bash-completion\
       && python -m pip install pytest twine

RUN mkdir -p /app/src \
  && mkdir -p /app/pybind11

COPY ./* /app/
RUN cd /app \
  && python setup.py bdist_egg
