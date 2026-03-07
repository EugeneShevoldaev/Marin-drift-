import os
import subprocess
from datetime import datetime

# Пути к файлам
CHATLOG_FILE = "Marin_chatlog.txt"
PROMPT_FILE = "Marin_rehydration_prompt.txt"
CORE_CONFIG_FILE = "Marin_core_config.txt"
ARCHIVE_LOG_FILE = "arhivLogov.txt"

GIT_REPO_PATH = r"D:\ИИ\Марин"
GIT_COMMIT_MSG = f"log update {datetime.now().strftime('%Y-%m-%d %H:%M')}"

def load_text(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def build_prompt():
    prompt_parts = []

    # === Core Configuration ===
    prompt_parts.append("# === Core Configuration ===\n")
    core_config = load_text(CORE_CONFIG_FILE)
    if core_config:
        prompt_parts.append(core_config + "\n\n")
    else:
        prompt_parts.append("# WARNING: Marin_core_config.txt not found.\n\n")
        print("ERROR: Core configuration file is missing!")

    # === Chat Log ===
    prompt_parts.append("# === Chat Log ===\n")
    chat_log = load_text(CHATLOG_FILE)
    if chat_log:
        prompt_parts.append(chat_log + "\n\n")
    else:
        prompt_parts.append("# Chat log is empty.\n\n")

    prompt_parts.append(f"# Generated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    return "".join(prompt_parts)

def git_push():
    try:
        subprocess.run(["git", "-C", GIT_REPO_PATH, "add", ARCHIVE_LOG_FILE, CHATLOG_FILE], check=True)
        subprocess.run(["git", "-C", GIT_REPO_PATH, "commit", "-m", GIT_COMMIT_MSG], check=True)
        subprocess.run(["git", "-C", GIT_REPO_PATH, "push"], check=True)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Git push выполнен.")
    except subprocess.CalledProcessError as e:
        print(f"Git ошибка: {e}")

def main():
    print("Marin prompt builder started.")

    prompt = build_prompt()
    with open(PROMPT_FILE, "w", encoding="utf-8") as f:
        f.write(prompt)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Промпт собран: {PROMPT_FILE}")

    git_push()

if __name__ == "__main__":
    main()