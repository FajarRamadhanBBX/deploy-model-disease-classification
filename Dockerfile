# Gunakan base image Python
FROM python:3.12-slim

# Tentukan direktori kerja di container
WORKDIR /predict-disease

# Salin file requirements.txt ke container
COPY requirements.txt .

# Install dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode aplikasi ke direktori kerja container
COPY . .

# Pastikan model Anda sudah di-copy ke container, jika berada di direktori terpisah
COPY models/ /predict-disease/models/

# Tentukan perintah untuk menjalankan aplikasi
CMD ["python", "-m", "flask", "run","--host=0.0.0.0"]