import subprocess

if __name__ == '__main__':
    while True:
        try:
            # subprocess.run(["/home/str/13ulan/.venv/bin/python", "/home/str/13ulan/start_all_bot.py"])
            subprocess.run(["/home/str/13ulan/.venv/bin/python", r"/home/str/13ulan/start_all_bot.py"])
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Ошибка: {e}")
