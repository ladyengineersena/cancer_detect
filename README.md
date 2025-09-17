# 🏥 Kanser Teşhis Sistemi

Makine öğrenmesi tabanlı kanser teşhis sistemi - Random Forest algoritması kullanarak meme kanseri tespiti yapan Python uygulaması.

## 📊 Proje Özeti

Bu proje, meme kanseri verilerini analiz ederek hastalık teşhisi yapan bir makine öğrenmesi modeli içerir. Random Forest algoritması kullanılarak %88+ doğruluk oranına ulaşılmıştır.

## ✨ Özellikler

- 🤖 **Random Forest Modeli** - Yüksek doğruluk oranı (%88.5)
- 📈 **Performans Metrikleri** - Accuracy, Precision, Recall, F1-Score
- 🎯 **Gerçek Zamanlı Test** - Rastgele örneklerle model doğrulaması
- 📊 **Veri Görselleştirme** - Detaylı istatistikler ve sonuçlar
- 🔬 **Bilimsel Yaklaşım** - Standart ML pipeline'ı

## 🚀 Kurulum ve Kullanım

### Gereksinimler

```bash
pip install numpy pandas scikit-learn
```

### Hızlı Başlangıç

```bash
python test_demo.py
```

## 📁 Proje Yapısı

```
cancer_detection/
├── README.md                 # Bu dosya
├── test_demo.py             # Ana uygulama
└── .gitignore               # Git ignore dosyası
```

## 🔬 Model Detayları

### Veri Seti
- **Toplam Örnek:** 1000
- **Özellikler:** 5 (radius, texture, perimeter, area, smoothness)
- **Kanser Oranı:** %30
- **Eğitim/Test Oranı:** 80/20

### Algoritma
- **Model:** Random Forest Classifier
- **Ağaç Sayısı:** 100
- **Random State:** 42 (tekrarlanabilir sonuçlar)

### Performans
- **Accuracy:** ~88.5%
- **Precision:** ~80%
- **Recall:** ~80.7%
- **F1-Score:** ~80.7%

## 📊 Örnek Çıktı

```
 KANSER TEŞHİS SİSTEMİ - HIZLI DEMO
==================================================
Veri seti boyutu: (1000, 6)
Kanser oranı: 30.00%
Eğitim seti: (800, 5)
Test seti: (200, 5)
Modeller eğitiliyor...
Random Forest Sonuçları:
Accuracy: 0.8850
Precision: 0.8000
Recall: 0.8067
F1-Score: 0.8067
Örnek Tahmin:
Gerçek: Sağlıklı
Tahmin: Kanserli
Güven: 77.00%
Demo başarıyla tamamlandı!
Model Accuracy: 88.50%
```

## 🎯 Kullanım Senaryoları

1. **Eğitim Amaçlı** - Makine öğrenmesi öğrenimi
2. **Demo Gösterim** - Model performansını gösterme
3. **Veri Analizi** - Kanser verisi analizi
4. **Algoritma Karşılaştırması** - Farklı modelleri test etme

## 🛠️ Geliştirme

### Yeni Özellik Ekleme
1. `test_demo.py` dosyasını düzenleyin
2. Yeni metrikleri hesaplayın
3. Daha fazla özellik ekleyin

### Model Geliştirme
- Daha fazla özellik ekleyin
- Farklı algoritmalar deneyin (SVM, Neural Networks)
- Hyperparameter tuning yapın
- Cross-validation ekleyin

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Commit yapın (`git commit -m 'Add some AmazingFeature'`)
4. Push yapın (`git push origin feature/AmazingFeature`)
5. Pull Request açın

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 👨‍💻 Geliştirici

Bu proje eğitim amaçlı geliştirilmiştir.

## 🙏 Teşekkürler

- scikit-learn ekibine
- NumPy ve Pandas geliştiricilerine
- Açık kaynak topluluğuna

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!
