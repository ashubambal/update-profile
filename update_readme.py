from datetime import datetime

with open("README.md", "r") as f:
    content = f.read()

updated_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
new_content = content.replace("🕒 Last Updated: <!-- last_updated -->", 
                              f"🕒 Last Updated: {updated_time} <!-- last_updated -->")

with open("README.md", "w") as f:
    f.write(new_content)
