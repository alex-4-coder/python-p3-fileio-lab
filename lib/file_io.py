# lib/file_io.py

def write_file(file_name, file_content):
    """Creates or overwrites a .txt file with the given content."""
    with open(f"{file_name}.txt", "w") as f:
        f.write(file_content)


def append_file(file_name, append_content):
    """Appends content to the end of the .txt file."""
    with open(f"{file_name}.txt", "a") as f:
        f.write(append_content)


def read_file(file_name):
    """Reads and returns the content of the .txt file."""
    with open(f"{file_name}.txt", "r") as f:
        return f.read()
