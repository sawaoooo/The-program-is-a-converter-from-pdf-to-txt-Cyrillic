import pytesseract
from pdf2image import convert_from_path

# Укажи путь к PDF
pdf_path = "/Users/sawa/Downloads/111.png.pdf"

# Конвертация PDF в изображения
images = convert_from_path(pdf_path)

# Распознавание текста
text = ""
for img in images:
    text += pytesseract.image_to_string(img, lang="rus+eng") + "\n"

# Сохранение в файл
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Текст сохранен в output.txt")
