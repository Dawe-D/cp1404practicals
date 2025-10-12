"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    file_data = load_data(FILENAME)
    print(display_details(file_data))


def display_details(file_data: list):
    subject_statement = ""
    for subject_data in file_data:
        subject_code = subject_data[0]
        subject_lecturer = subject_data[1]
        number_of_students = subject_data[2]
        subject_statement += f"{subject_code} is taught by {subject_lecturer} and has {number_of_students: 3} students\n"
    return subject_statement


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    file_data = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        file_data.append(parts)
    input_file.close()
    return file_data

main()
