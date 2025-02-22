**PDF to Text Converter**
Этот скрипт конвертирует PDF-файл в изображения, распознает текст с помощью Tesseract OCR и сохраняет результат в output.txt.

**🔧 Требования**
Перед запуском убедитесь, что у вас установлены:

Python 3.x
pytesseract
pdf2image
Tesseract OCR

**Установка зависимостей**
bash
Copy
Edit
pip install pytesseract pdf2image

**Дополнительно установите Tesseract OCR:**

macOS (через Homebrew):
bash
Copy
Edit
brew install tesseract
Ubuntu/Debian:
bash
Copy
Edit
sudo apt install tesseract-ocr

**Windows: скачать и установить**
🚀 Запуск
Укажите путь к PDF-файлу в переменной pdf_path в коде.
Запустите скрипт:
bash
Copy
Edit
python script.py
После выполнения текст будет сохранен в output.txt.

**📝 Как это работает**
PDF конвертируется в изображения с помощью pdf2image.
pytesseract распознает текст на русском и английском языках.
Результат сохраняется в output.txt.

**📌 Примечания**
Поддерживаются многостраничные PDF-файлы.
При необходимости можно изменить языки OCR, добавив или убрав lang="rus+eng".
