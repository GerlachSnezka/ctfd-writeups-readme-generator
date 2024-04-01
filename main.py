import requests

def fetch_challenge_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch challenge data.")
        return None

def generate_readme(challenges):
    categories = {}
    for challenge in challenges:
        category = challenge['category']
        if category not in categories:
            categories[category] = []
        categories[category].append(challenge)

    readme_content = ""
    for category, challenges in categories.items():
        readme_content += f"### {category}\n"
        for challenge in challenges:
            solved = "✔" if challenge['solved_by_me'] else "❌"
            readme_content += f"- **{challenge['name']}** ({challenge['value']} points) {solved}\n"
        readme_content += "\n"

    return readme_content

def main():
    url = input("Enter the URL to fetch challenge data: ")
    challenge_data = fetch_challenge_data(url)
    if challenge_data:
        readme_content = generate_readme(challenge_data['data'])
        with open("README.md", "w") as file:
            file.write(readme_content)
        print("README.md generated successfully.")
    else:
        print("Failed to generate README.")

if __name__ == "__main__":
    main()
