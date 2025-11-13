# cicd-flask: CI/CD пайплайн для Python-приложения

Данный репозиторий базовый цикл CI/CD (Continuous Integration / Continuous Deployment) для простого веб-приложения на Flask.

Приложение контейнеризировано с помощью Docker и автоматически собирается, тестируется (линтером) и публикуется в GitHub Container Registry (GHCR) с помощью GitHub Actions.

## Что было сделано

* **Приложение:** Простое Python-приложение на **Flask** с тремя эндпоинтами:
    * `/`: Главная страница.
    * `/health`: Эндпоинт для проверки "здоровья" сервиса.
    * `/metrics`: Заглушка для метрик в формате Prometheus.
* **Контейнеризация:**
    * Написан `Dockerfile` для сборки production-образа.
    * Написан `docker-compose.yml` для удобного локального запуска и разработки.
* **CI/CD Пайплайн:** Настроен пайплайн в `.github/workflows/ci-cd.yml`, который:
    1.  **Запускается** при каждом `push` в ветку `main`.
    2.  **Lint (`lint`)**: Проверяет код на соответствие стилю (PEP 8) с помощью `flake8`.
    3.  **Build & Push (`build_and_push`)**: В случае успеха шага `lint`, собирает Docker-образ и публикует его в GitHub Container Registry (GHCR).

## Как проверить

Есть два способа запустить этот проект:

### 1. Локальная разработка (из исходного кода)

Этот способ использует `docker-compose.yml` и идеально подходит для внесения изменений в код.

1.  Клонируйте репозиторий:
    ```bash
    git clone https://github.com/wispyth/cicd-flask.git
    cd cicd-flask
    ```
2.  Запустите сервисы:
    ```bash
    docker compose up --build
    ```
3.  Откройте в браузере `http://localhost:5000`. Вы должны увидеть "test CI/CD".

### 2. Запуск готового образа (из GHCR)

Этот способ использует образ, который был автоматически собран  CI/CD пайплайном.

1.  Скачайте образ:
    ```bash
    docker pull ghcr.io/wispyth/cicd-flask:latest
    ```
2.  Запустите контейнер:
    ```bash
    docker run -d -p 5000:8000 --name flask-app ghcr.io/wispyth/cicd-flask:latest
    ```
3.  Откройте в браузере `http://localhost:5000`.

### Проверка эндпоинтов

После запуска любым из способов, вы можете проверить все эндпоинты:

* `http://localhost:5000/`
* `http://localhost:5000/health`
* `http://localhost:5000/metrics`