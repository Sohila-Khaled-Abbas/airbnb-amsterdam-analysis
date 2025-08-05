FROM bitnami/spark:3.3.0-debian-11-r0

WORKDIR /app

USER root
RUN apt-get update && apt-get install -y python3 python3-pip && ln -s /usr/bin/python3 /usr/bin/python
RUN pip3 install pyspark
USER 1001

COPY etl/pyspark_modeling.py /app/
COPY data/processed/cleaned_listings.csv /app/
COPY data/processed/cleaned_calendar.csv /app/
COPY data/processed/cleaned_reviews.csv /app/

CMD ["python", "pyspark_modeling.py"]