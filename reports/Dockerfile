FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "-m", "case-study-2-drift-detector.src.cli", "run", "./case-study-2-drift-detector/data"]

