import os
import shutil
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_folder> <output_folder>")
        return

    source_folder = sys.argv[1]
    output_folder = sys.argv[2]

    if not os.path.exists(source_folder):
        print('The source folder doesn\t exist kindly make sure that you directory exist')
        return 

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each file in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith(".txt"):
            language, _ = filename.split("-")
            language_folder = os.path.join(output_folder, language)

            # Create a sub-folder for the language if it doesn't exist
            if not os.path.exists(language_folder):
                os.makedirs(language_folder)

            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(language_folder, filename)

            # Move the file to the appropriate sub-folder
            shutil.move(source_file, destination_file)

    print("Files grouped into sub-folders based on language.")

if __name__ == "__main__":
    main()