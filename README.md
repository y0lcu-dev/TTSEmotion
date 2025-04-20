# Duygu Kontrollü Türkçe Metinden Sese Dönüştürme Sistemi

Bu proje, TextrolSpeech framework'ünü temel alarak Türkçe dilinde duygu ve konuşma tarzı kontrollü bir Metinden Sese (Text-to-Speech - TTS) sistemi geliştirmeyi amaçlamaktadır.

## 📌 Proje Özeti
Projemiz, mevcut TextrolSpeech mimarisini uygulayıp genişleterek:
- Prompt tabanlı konuşma stilini ve duygu kontrolünü gerçekleştirecek,
- Öğrencilerden ve sosyal medya platformlarından elde edilen ses kayıtlarıyla bir Türkçe ses veri seti oluşturacak,
- Veri setini metin bazlı duygu etiketleriyle zenginleştirecek,
- Codec tabanlı TTS modelleme yöntemlerini kullanacaktır.

## 🚀 Özellikler
- Türkçe dilinde duygu kontrollü sentetik ses üretimi
- Çoklu konuşma tarzları ve tonlama seçenekleri
- Sosyal medya ve öğrenci tabanlı Türkçe veri seti
- Multilingual ve ekspresif ses sentezi

## 🛠️ Kullanılan Teknolojiler
- **TextrolSpeech Framework**
- **Prompt Tabanlı Duygu ve Stil Kontrolü**
- **Codec Tabanlı TTS Modelleme**

## 🎙️ Veri Seti
Veri seti olarak TurEV-DB kullanılacaktır, aynı zamanda modelin dahada zenginleştirebilmek için öğrencilerden ses kayıtları elde edilecektir:
- Öğrencilerden toplanan ses kayıtları
- Sosyal medyadan elde edilen ses örnekleri
- Metin bazlı duygu etiketlemeleri

## 🔧 Kurulum ve Kullanım
*(Burada projenin kurulumu ve kullanımıyla ilgili detaylı bilgiler yer alacaktır.)*

## 📂 Repository Yapısı
```
proje/
├── TurEV-DB/          # Türkçe duygu etiketli veri seti
├── models/            # Eğitilmiş TTS modelleri
├── data_extraction/   # Veri ön işleme ve eğitim scriptleri
├── results/           # Eğitim sonuçları ve demo ses örnekleri
└── docs/              # Dökümantasyon ve kullanım kılavuzları
```