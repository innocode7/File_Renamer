import os

def rename_files_in_directory(directory, old_text, new_text):
    try:
        # List all files in the specified directory
        files = os.listdir(directory)

        for filename in files:
            # Check if the file name contains the old text
            if old_text in filename:
                # Create the new file name by replacing the old text with the new text
                new_filename = filename.replace(old_text, new_text)

                # Create full paths for the old and new file names
                old_file = os.path.join(directory, filename)
                new_file = os.path.join(directory, new_filename)

                # Rename the file
                os.rename(old_file, new_file)
                print(f'Renamed: {filename} -> {new_filename}')

        print('All files have been renamed successfully.')
    except Exception as e:
        print(f'An error occurred: {e}')

# Specify the directory, old text, and new text
directory = r'C:\Users\kevin\Downloads\content_2024'
old_text = '기획자를 위한 노코드 AI챗봇 만들기'
new_text = '노코드 AI챗봇 만들기'

# Call the function to rename files
rename_files_in_directory(directory, old_text, new_text)
