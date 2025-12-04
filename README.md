# ♻ SmartWasteApp – Akıllı Atık Yönetimi ve Geri Dönüşüm Takip Uygulaması

Bu proje, geri dönüşüm bilincini artırmak ve bireylerin günlük atık miktarlarını takip etmelerini sağlamak amacıyla geliştirilmiş web tabanlı bir akıllı atık yönetimi uygulamasıdır. 

Sosyal Sorumluluk dersi kapsamında hazırlanmış olup; modern arayüz, grafiksel istatistikler, CSV dışa aktarma, rozet sistemi ve admin paneli gibi gelişmiş özellikler içermektedir.

---

## 🚀 Özellikler

- **Atık Kayıt Sistemi:**  
  Kullanıcılar isim, tarih, kategori ve miktar girerek kayıt oluşturabilir.

- **Rozet Sistemi:**  
  Girilen atık miktarına göre motive edici rozetler gösterilir (örn. “Plastik Ustası 🏅”).

- **İstatistiksel Grafikler:**  
  Chart.js ile pasta grafik ve çubuk grafik — kategori bazlı toplam atık miktarları.

- **Kayıt Yönetimi:**  
  Kayıtları görüntüleme, silme ve CSV olarak dışa aktarma.

- **Admin Paneli:**  
  Tüm kayıtları yöneten basit yönetim paneli.

- **Dark Mode:**  
  Üst menüdeki toggle ile açık/koyu tema arasında geçiş.

- **Modern UI / UX:**  
  Bootstrap 5 ve özel CSS ile geliştirilmiş premium arayüz.

---

## 🖥️ Teknolojiler

- Python
- Flask Framework
- SQLite Veritabanı
- Bootstrap 5
- Chart.js
- HTML5 / CSS / JS

---

## 📦 Kurulum

```bash
git clone https://github.com/kullaniciadiniz/SmartWasteApp.git
cd SmartWasteApp
python -m venv venv
venv\Scripts\activate
pip install flask flask_sqlalchemy
python app.py

Uygulama daha sonra şu adreste çalışır:

http://127.0.0.1:5001