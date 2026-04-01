# 🛡️ CrystalDefence — Пуленепробиваемое стекло для гражданских лиц

Премиальное веб-приложение для продажи защитных стекол класса 4 с современным dark-themed дизайном.

## 🌟 Особенности проекта

### 🎨 Дизайн
- **Dark Theme** премиум-класса с градиентными акцентами
- Минималистичный стиль в духе https://vaonis.com/
- Строгие линии и технологичная эстетика
- Адаптивная верстка (mobile-first)

### 🛠️ Технологии
- **HTML5** + CSS3 Grid/Flexbox
- **Jinja2** шаблоны с переменным контекстом
- **Intersection Observer API** для анимаций при скролле
- Чистый JavaScript без библиотек

### 📱 Адаптивность
- Поддержка всех breakpoints (1024px, 768px, 480px)
- Flexbox/Grid для динамической сетки
- Fluid typography с clamp()

## 📁 Структура проекта

```
CrystalDefence_Site/
├── src/
│   ├── static/
│   │   ├── style.css          # Премиум стили dark theme
│   │   └── videos/            # Видео-контент (опционально)
│   │       └── .README.md     # Инструкция по загрузке видео
│   └── templates/
│       ├── base.html          # Базовый шаблон с навигацией
│       ├── index.html         # Главная страница
│       ├── products.html      # Каталог продукции
│       └── about.html         # О компании
├── README.md                  # Документация проекта
└── .nojekyll                  # Для GitHub Pages
```

## 🚀 Быстрый старт

### Локальная разработка

1. Запустите локальный сервер:
```bash
# Python 3
python -m http.server 8000

# Или Node.js с live-reload
npm install -g serve && serve .
```

2. Откройте `http://localhost:8000` в браузере

### GitHub Pages (деплой)

1. Добавьте файл `.nojekyll` в корне репозитория (уже есть)
2. В настройках GitHub → Pages выберите ветку с файлами
3. Сайт будет доступен по адресу: `https://username.github.io/repository-name/`

## 🎬 Видео-контент

### Добавление фона для hero секции

1. Загрузите видео в `/src/static/videos/hero-bg.mp4`:
   - Размер ≤ 5MB
   - Формат MP4, H.264
   - Разрешение 1920x1080 или 1280x720

2. Или используйте онлайн-заглушку:
```html
<source src="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4">
```

3. Для статичного фона замените `<video>` на `<img>`:
```html
<img class="hero-bg-image" src="/static/images/hero-bg.jpg" alt="">
```

## 🎨 CSS Классы для разработчиков

### Анимации появления при скролле

```html
<!-- Fade In Up -->
<div class="fade-up">...</div>

<!-- Для JS Intersection Observer -->
<div class="fade-up fade-in-up" id="hero-title">...</div>
```

### Hero секции с видео

```html
<section class="hero hero-dark">
  <div class="hero-video-container">
    <video autoplay muted loop playsinline>
      <source src="/static/videos/hero-bg.mp4" type="video/mp4">
    </video>
  </div>
  <div class="hero-overlay"></div>
  <div class="hero-content">...</div>
</section>
```

### CTA контейнеры

```html
<div class="cta-container">
  <h3>Заголовок призыва к действию</h3>
  <p>Описание преимущества или предложение</p>
</div>
```

## 📄 Шаблоны Jinja2

### Переменные в шаблонах

```jinja2
{# index.html #}
{% include 'base.html' %}
<body page="index">
  {% block content %}
    <!-- Ваш контент -->
  {% endblock %}
</body>
```

### Базовая структура (base.html)

```html
{% extends "base.html" %}
{% block title %}Заголовок страницы{% endblock %}
{% block content %}Контент страницы{% endblock %}
```

## 🎯 Преимущества перед стандартными решениями

| Функция | Реализация | Статус |
|---------|-----------|--------|
| Dark Theme | Градиенты, акцентные цвета | ✅ |
| Video Hero | Контейнеры для видео | ✅ |
| Scroll Animations | Intersection Observer | ✅ |
| Mobile-first | Responsive breakpoints | ✅ |
| CSS Grid/Flexbox | Адаптивные сетки | ✅ |
| Header scrolled state | JS observer | ✅ |

## 🔧 Конфигурация

### Переменные CSS в :root

```css
--primary-bg: #0f172a;          /* Основной фон */
--accent-primary: #38bdf8;      /* Primary акцент */
--accent-secondary: #2dd4bf;    /* Secondary акцент */
--text-primary: #f1f5f9;        /* Основной текст */
--border-color: rgba(134, 132, 132, 0.1);  /* Цвет границ */
```

## 📊 Производительность

### Оптимизация видео
- Сжимайте через `ffmpeg`:
```bash
ffmpeg -i input.mp4 -vf "scale=1280:720" -c:v libx264 -crf 23 output.mp4
```

### Lazy loading для изображений
```html
<img src="/path.jpg" loading="lazy" alt="">
```

## 🎓 Ресурсы

- [Intersection Observer API](https://developer.mozilla.org/ru/docs/Web/API/Intersection_Observer_API)
- [CSS Custom Properties](https://developer.mozilla.org/ru/docs/Web/CSS/Using_CSS_custom_properties)
- [Jinja2 documentation](https://jinja.palletsprojects.com/)

## 📝 Лицензия

MIT License — свободное использование для коммерческих и личных проектов.

---

**Версия:** 1.0.0  
**Обновлено:** 2024  
**Разработано:** CrystalDefence Team
