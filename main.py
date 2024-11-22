import tkinter as tk
import subprocess

def save_and_run():
    inputLocal = entryLocal.get()
    inputGit = entryGit.get()
    global localPath, GitPath
    localPath = inputLocal
    GitPath = inputGit

    commands = [
        "git --version", # проверяем что git установлен
        "cd \\",  # переходим в корневую папку
        "cd " + localPath,  # переходим в локальную папку с проектом
        "git init",  # инициализируем локальный git репозиторий
        "git add .",  # добавляем в него все файлы из проекта
        "git commit -m First",  # создаем первый коммит
        f"git remote add origin {GitPath}",  # связываем локальный и удаленный репозиторий
        "git branch -M main",  # переименовываем ветку в main
        "git push -u origin main"  # отправляем проект на  GitHub
    ]

    for command in commands:
        print(f"Выполняется команда: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=localPath)
        if result.returncode != 0:
            print(f"Ошибка при выполнении '{command}': {result.stderr}")
            break
        else:
            print(f"Успешно выполнено: {result.stdout}")

    label_result.config(text="Данные сохранены:\nЛокальный путь: " + localPath + "\nGit путь: " + GitPath)

# Создаем главное окно
root = tk.Tk()
root.title("New Git Project")
root.geometry("300x250")

labelLocal = tk.Label(root, text="Введите путь к локальному репозиторию: ")
labelLocal.pack(pady=10)
entryLocal = tk.Entry(root, width=30)
entryLocal.pack(pady=5)

labelGit = tk.Label(root, text="Введите путь к Git репозиторию: ")
labelGit.pack(pady=10)
entryGit = tk.Entry(root, width=30)
entryGit.pack(pady=5)

# Создаем кнопку для сохранения данных
button_save = tk.Button(root, text="Загрузить", command=save_and_run)
button_save.pack(pady=10)

# Метка для отображения результата
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Запускаем главный цикл
root.mainloop()