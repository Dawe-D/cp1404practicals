"""
CP1404 - Prac 7
Task - Project Management
Time
Estimate - 90 mins  Actual - 120 mins
"""

from project import Project
from operator import attrgetter
import datetime

FILE_NAME = "projects.txt"
MENU = (f"Menu: \n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects"
        f"\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project \n- (Q)uit")


def main():
    """Manage a list of projects."""
    print("Welcome to Pythonic Project Management")
    projects = []
    # projects = load_projects(FILE_NAME)
    # print(f"Loaded {len(projects)} projects from {FILE_NAME}")
    print(MENU)
    choice = input(">>> ").upper().strip()

    while choice != "Q":
        if choice == "L":
            file_name = input("Enter filename to load projects from: ").strip()
            try:
                projects = load_projects(file_name)
                print(f"Loaded {len(projects)} projects from {file_name}")
            except FileNotFoundError:
                print(f"File '{file_name}' not found. Projects not changed.")

        elif choice == "S":
            if not projects:
                print("No projects to save.")
            else:
                save_file_name = input("Enter filename to save projects to: ").strip()
                save_projects(save_file_name, projects)

        elif choice == "D":
            display_projects(projects)

        elif choice == "F":
            filter_projects_by_date(projects)

        elif choice == "A":
            add_project(projects)

        elif choice == "U":
            update_project(projects)

        else:
            print("Invalid menu choice")

        print(MENU)
        choice = input(">>> ").upper().strip()

    if choice == "Q":
        save_choice = input(f"Save to default file ({FILE_NAME}) before quitting? (Y/N): ").strip().upper()
        if save_choice == "Y":
            save_projects(FILE_NAME, projects)
        print("Goodbye!")



def load_projects(filename):
    """Load projects from a file and return a list of project objects."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split('\t')
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def display_projects(projects):
    """Display projects, sorted and in categories of completion status."""
    incomplete_projects = [project for project in sorted(projects) if not project.is_complete()]
    completed_projects = [project for project in sorted(projects) if project.is_complete()]

    if incomplete_projects:
        print("Incomplete projects:")
        for project in incomplete_projects:
            print("", project)
    else:
        print("No incomplete projects.")

    if completed_projects:
        print("Completed projects:")
        for project in completed_projects:
            print("", project)
    else:
        print("No completed projects.")


def filter_projects_by_date(projects):
    """Filter projects to display only those after a certain date."""
    date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
    projects_after_date = [project for project in sorted(projects, key=attrgetter('start_date')) if
                           project.start_date > date]
    for project in projects_after_date:
        print(project)
    if not projects_after_date:
        print(f"There are no projects that started after {date.strftime("%d/%m/%Y")}")


def get_valid_date(prompt):
    """Prompt the user for a valid date (dd/mm/yyyy) and return a datetime.date object."""
    while True:
        date_string = input(prompt)
        try:
            return datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        except ValueError:
            print("Invalid date format. Please use dd/mm/yyyy.")


def user_project_input():
    """Get user input for a new project and return a Project object."""
    name = input("Project name: ")
    start_date = get_valid_date("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, completion_percentage)


def update_project(projects):
    """ Allow the user to update the completion percentage and priority of a project."""
    for i, project in enumerate(projects, 1):
        print(f"{i}: {project}")
    choice = int(input("Project choice(number): "))
    project = projects[choice - 1]
    print("Selected: ", project)

    new_percentage = input("New Percentage (leave blank to keep current): ").strip()
    if new_percentage != "":
        try:
            project.completion_percentage = int(new_percentage)
        except ValueError:
            print("Invalid percentage. Keeping current value.")
    else:
        print("Keeping current percentage")

    new_priority = input("New Priority (leave blank to keep current): ").strip()
    if new_priority != "":
        try:
            project.priority = int(new_priority)
        except ValueError:
            print("Invalid priority. Keeping current value.")
    else:
        print("Keeping current priority")

    print("Updated project: ", project)


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                           f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"{len(projects)} projects saved to {filename}")


def add_project(projects):
    """Add a new project to the list."""
    project = user_project_input()
    projects.append(project)
    print(f"Project '{project.name}' added.")


if __name__ == "__main__":
    main()
