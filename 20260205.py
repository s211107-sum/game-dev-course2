# my_portfolio.py

def print_line(char='-', length=50):
    print(char * length)

def header(title):
    print_line('=')
    print(f"{title:^50}")
    print_line('=')

def section(title, content):
    print(f"\n{title}")
    print_line('-')
    print(content)

def main():
    # Header
    header("Hello World - Python Portfolio")

    # About Me
    about_content = (
        "Hi! I'm Alex Doe, a Python developer passionate about automation, data science, and clean code.\n"
        "I enjoy building projects that make life easier using simple, elegant Python scripts."
    )
    section("About Me", about_content)

    # Skills
    skills = [
        "✔ Python 3",
        "✔ Automation (scripting, bots)",
        "✔ Data Analysis (Pandas, Matplotlib)",
        "✔ Web Development (Flask, FastAPI)",
        "✔ SQL, Git, and APIs"
    ]
    skills_content = "\n".join(skills)
    section("Skills", skills_content)

    # Projects
    projects = [
        "📊 Budget Tracker - CLI tool to track expenses",
        "🕸 Web Scraper - Extracts data from websites",
        "📁 File Organizer - Auto-sorts files by type/date",
        "🤖 Discord Bot - Custom bot for server automation"
    ]
    projects_content = "\n".join(projects)
    section("Projects", projects_content)

    # Contact
    contact_content = (
        "Email   : alexdoe@example.com\n"
        "GitHub  : github.com/alexdoe\n"
        "LinkedIn: linkedin.com/in/alexdoe"
    )
    section("Contact", contact_content)

    print("\nThank you for viewing my portfolio!\n")

if __name__ == "__main__":
    main()