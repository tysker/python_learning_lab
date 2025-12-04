STARTING_LETTER_PATH = "./input/letters/starting_letter.txt"
READY_TO_SEND_PATH = "./output/readytosend"
INVITED_NAMES_PATH = "./names/invited_names.txt"


def read_from_file(file_path):
    with open(file_path) as text:
        # could use also readlines()
        return text.read()


def write_to_file(file_path, letter):
    with open(file_path, mode="w") as file:
        file.write(letter)


def update_file_with_names(text, name):
    return text.replace("[name]", name)


def save_files_with_new_names():
    # Get letter text
    letter = read_from_file(STARTING_LETTER_PATH)

    # Get names and append names to array
    names_text = read_from_file(INVITED_NAMES_PATH)
    names = [n.strip() for n in names_text.splitlines() if n.strip()]

    # Loop through names array and write a letter for each name
    for name in names:
        updated_letter = update_file_with_names(letter, name)
        write_to_file(
            f"{READY_TO_SEND_PATH}/{name.lower()}_invitation.txt", updated_letter
        )


save_files_with_new_names()
