# 💻 MVS-Dev | Developer Portfolio

[![Live Site](https://img.shields.io/badge/▶_Live_Site-mvs--dev.com-10b981?style=for-the-badge&logoColor=white)](https://mvs-dev.com)

A personal developer portfolio with a retro terminal / phosphor-green CRT aesthetic. Showcases projects in an interactive 3D coverflow carousel and includes a contact form that delivers messages straight to Telegram.

![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Alpine.js](https://img.shields.io/badge/Alpine.js-8BC0D0?style=flat-square&logo=alpinedotjs&logoColor=black)
![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram_Bot-26A5E4?style=flat-square&logo=telegram&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Caddy](https://img.shields.io/badge/Caddy-1F88C0?style=flat-square&logo=caddy&logoColor=white)

---

## 🚀 Key Features

* **3D Coverflow Carousel:** Interactive project showcase with depth, navigated via side arrows and keyboard.
* **Managed Content:** Projects are created and edited through the Django admin (title, description, posters, links, demo/live status).
* **Contact Form → Telegram:** Submissions are validated server-side and instantly forwarded to a Telegram chat via the Bot API.
* **Retro Terminal UI:** Phosphor-green CRT styling — scanlines, animated particles, decrypting name effect.

---

## 🛠️ Tech Stack

* **Backend:** Django
* **Database:** PostgreSQL
* **Frontend:** Django Templates + Alpine.js + Tailwind (CDN)
* **Notifications:** Telegram Bot API (via stdlib `urllib`, no extra deps)
* **Web Server:** Gunicorn (WSGI)
* **Reverse Proxy:** Caddy (automatic SSL/HTTPS)
* **Containerization:** Docker & Docker Compose

---

## 🏗️ Architecture

Managed by **Docker Compose**:

* `mvs_web` — Django application: project catalog, admin, and the contact endpoint (Gunicorn).
* `mvs_db` — PostgreSQL with a persistent volume.

A shared **Caddy** container (separate compose project) is the single entry point on ports 80/443. It serves `/static` and `/media` directly from volumes and proxies everything else to Django, handling SSL certificates automatically.