# TestWork

## Инструкция по запуску

1. Клонируйте репозиторий и перейдите в директорию проекта
2. Создайте виртуальное окружение и активируйте его
3. Установите зависимости: pip install -r requirements.txt
4. Создайте файл .env в корневой директории проекта, в него поместите:
   LOGIN=standard_user
   PASSWORD=secret_sauce
6. Запустите тесты:
   - Базовый запуск: pytest
   - Развернутый запуск: pytest -v
   - С Allure отчетом: pytest --alluredir=allure-results && allure serve allure-results
