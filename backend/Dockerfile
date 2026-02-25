FROM python:3.12-slim

WORKDIR /app
# Prevent pyc creation and enable direct logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# copy files of dependency
COPY pyproject.toml uv.lock* ./
# install or upgrade pip
RUN pip install --upgrade pip
# copy dependency
COPY requirements.txt .
# install dependency
RUN pip install -r requirements.txt

# copy source
COPY app ./app

EXPOSE 9000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000"]
