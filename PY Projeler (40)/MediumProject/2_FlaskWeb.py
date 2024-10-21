from flask import Flask, render_template, request  # Flask sınıflarını içe aktarır

app = Flask(__name__)  # Flask uygulamasını başlatır.

# Ana sayfa rotası
@app.route('/')
def ana_sayfa():
    return render_template('index.html')  # 'index.html' dosyasını render eder

# Form verisini işleyen rota
@app.route('/gonder', methods=['POST'])
def gonder():
    kullanici_adi = request.form['kullanici_adi']  # Formdan 'kullanici_adi' alanını alır
    return f"Merhaba, {kullanici_adi}!"

if __name__ == '__main__':
    app.run(debug=True)  # Uygulamayı debug modunda çalıştırır
