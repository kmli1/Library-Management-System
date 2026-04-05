# Library-Management-System
Library managment system
# 📚 Kütüphane Yönetim Sistemi / Library Management System (CLI)

*(For English, please scroll down)*

Bu proje, Nesne Yönelimli Programlama (OOP) prensipleri kullanılarak Python ile geliştirilmiş, komut satırı (CLI) tabanlı bir Kütüphane Otomasyon Sistemidir. Kitap ve üye yönetimi, ödünç alma/iade işlemleri gibi temel kütüphane fonksiyonlarını güvenli ve esnek bir mimariyle sunar.

## 🚀 Özellikler (TR)
* **Kapsamlı Materyal Yönetimi:** Kütüphaneye Roman, Dergi ve Çizgi Roman olmak üzere farklı türlerde materyal eklenebilir.
* **Üye Sistemi:** Yeni üyeler kaydedilebilir ve her üyenin kendi ödünç aldığı kitaplar listesi tutulur.
* **Ödünç / İade İşlemleri:** Stok kontrolü yapılarak kitaplar üyelere ödünç verilebilir ve iade alınabilir.
* **Akıllı Arama:** Kitaplar hem ISBN numarası üzerinden hem de başlık içindeki kelimelerden aranabilir.
* **Güvenli İşlem Akışı (Error Handling):** Hatalı veri girişleri veya kurallara aykırı işlemler (örn: zaten ödünçte olan bir kitabı tekrar ödünç vermeye çalışmak, sayı yerine harf girmek) özel Exception sınıflarıyla yakalanır ve programın çökmesi engellenir.

## 💻 Kullanılan Teknolojiler ve Mimari
Bu proje tamamen **Python 3** kullanılarak geliştirilmiştir. 
* **Kalıtım (Inheritance):** `Kitap` (Base Class) sınıfından türetilen `Roman`, `Dergi` ve `CizgiRoman` sınıfları aracılığıyla hiyerarşik bir yapı kurulmuştur.
* **Kapsülleme (Encapsulation):** Kitapların ISBN ve ödünç durumları gizlenerek (`__isbn`, `__odunc_alan`) dışarıdan doğrudan müdahaleye kapatılmıştır.
* **Özel Hata Yönetimi (Custom Exceptions):** Programın stabilitesini sağlamak için özel hata sınıfları (`KitapZatenOduncVerildiError`, `KitapBulunamadiError` vb.) tanımlanmıştır.

---

## 🇬🇧 English Description

This project is a Command Line Interface (CLI) based Library Automation System developed in Python, utilizing Object-Oriented Programming (OOP) principles. It provides a secure and flexible architecture for core library functions such as book and member management, borrowing, and returning processes.

## 🚀 Features (EN)
* **Comprehensive Material Management:** Different types of materials can be added to the library, including Novels, Magazines, and Comic Books.
* **Membership System:** New members can be registered, and a specific borrowed books list is maintained for each member.
* **Borrow / Return Operations:** Books can be lent to members and returned with real-time stock and availability checks.
* **Smart Search:** Books can be searched by their ISBN or by keywords in their titles.
* **Secure Workflow (Error Handling):** Invalid data entries or rule violations (e.g., trying to borrow a book that is already taken, entering letters instead of numbers) are caught using custom Exception classes, preventing the application from crashing.

## 💻 Technologies & Architecture
This project is developed entirely using **Python 3**, focusing on demonstrating OOP capabilities:
* **Inheritance:** A hierarchical structure is established via `Roman` (Novel), `Dergi` (Magazine), and `CizgiRoman` (Comic Book) classes inheriting from the base `Kitap` (Book) class.
* **Encapsulation:** Critical data such as ISBN and borrowing status are hidden (`__isbn`, `__odunc_alan`) to prevent direct external modification, ensuring data integrity.
* **Custom Exceptions:** Custom error classes (like `KitapZatenOduncVerildiError`, `KitapBulunamadiError`) are defined and handled within `try-except` blocks to ensure application stability.

