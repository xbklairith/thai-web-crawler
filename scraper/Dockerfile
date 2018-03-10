FROM python:2.7
RUN pip install scrapy
WORKDIR /app
RUN mkdir -p /var/output
ADD . .
VOLUME ["/var/output"]
CMD ["scrapy", "crawl", "momentum", "--output=/var/output/momentum.json"]