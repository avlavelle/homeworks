FROM python:3.8.10

RUN pip install Flask==2.2.0 redis requests
RUN pip install requests==2.22.0


ADD gene_api.py /gene_api.py

CMD ["python", "gene_api.py"]
