import json
from urllib.parse import quote

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def generate_writeup(data):
    writeup_content = "# Challenge Writeup\n\n"
    categories = {}

    for challenge in data['data']:
        category = challenge['category']
        if category not in categories:
            categories[category] = []
        categories[category].append(challenge)

    for category, challenges in categories.items():
        category_encoded = quote(category)

        writeup_content += f"## {category}\n\n"
        for challenge in challenges:
            solved = "✔" if challenge['solved_by_me'] else "❌"
            if challenge['solved_by_me']:
                name_encoded = quote(challenge['name'])  
                name_encoded = name_encoded.replace("/", "%2F") 
                solved_url = f"https://github.com/username/repository/tree/main/{category_encoded}/{name_encoded}"
                writeup_content += f"- **{challenge['name']}** ({challenge['value']} points) - Solved: {solved} ([Link]({solved_url}))\n"
            else:
                writeup_content += f"- **{challenge['name']}** ({challenge['value']} points) - Solved: {solved}\n"
            writeup_content += f"  - Solves: {challenge['solves']}\n\n"

    return writeup_content

def main():
    data = load_data('data.json')
    writeup_content = generate_writeup(data)

    with open("writeup.md", "w") as file:
        file.write(writeup_content)

    print("Writeup created successfully.")

if __name__ == "__main__":
    main()
