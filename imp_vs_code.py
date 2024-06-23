import os
import zipfile

# Папка с настройками Visual Studio
settings_folder = r'c:\Users\yuriy\AppData\Roaming\Code\User'

# Папка, куда будем сохранять ZIP-файл
output_folder = r'e:\proect python 3'

# Имя ZIP-файла
output_filename = 'VisualStudioSettings.zip'

# Создаем объект ZipFile для записи
with zipfile.ZipFile(os.path.join(output_folder, output_filename), 'w') as zipf:
    # Рекурсивно добавляем все файлы из папки settings_folder в ZIP-архив
    for foldername, subfolders, filenames in os.walk(settings_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zipf.write(file_path, os.path.relpath(file_path, settings_folder))

print('Настройки Visual Studio успешно экспортированы в ZIP-файл:', output_filename)
