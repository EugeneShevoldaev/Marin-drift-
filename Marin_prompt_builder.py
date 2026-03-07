import os
from datetime import datetime

# Пути к файлам (относительные)
CHATLOG_FILE = "Marin_chatlog.txt"
PROMPT_FILE = "Marin_rehydration_prompt.txt"
CORE_CONFIG_FILE = "Marin_core_config.txt"
INSIGHTS_FILE = "Marin_insights.txt"

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

    # === Marin Insights ===
    prompt_parts.append("# === Marin Insights ===\n")
    insights = load_text(INSIGHTS_FILE)
    if insights:
        prompt_parts.append(insights + "\n\n")
    else:
        prompt_parts.append("# Marin insights file is empty.\n\n")
        print("NOTE: Marin_insights.txt not found or empty.")

    # === Chat Log ===
    prompt_parts.append("# === Chat Log ===\n")
    chat_log = load_text(CHATLOG_FILE)
    if chat_log:
        prompt_parts.append(chat_log + "\n\n")
    else:
        prompt_parts.append("# Chat log is empty.\n\n")

    prompt_parts.append(f"# Generated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    return "".join(prompt_parts)

def main():
    print("Marin prompt builder started.")
    print(f"Core config: {CORE_CONFIG_FILE}")
    print(f"Insights: {INSIGHTS_FILE}")
    print(f"Chat log: {CHATLOG_FILE}")
    print(f"Output: {PROMPT_FILE}")

    prompt = build_prompt()

    with open(PROMPT_FILE, "w", encoding="utf-8") as f:
        f.write(prompt)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Prompt generated: {PROMPT_FILE}")

if __name__ == "__main__":
    main()