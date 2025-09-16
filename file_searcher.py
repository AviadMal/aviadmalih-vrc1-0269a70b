import os

def find_file(filename, search_path):
    """
    Search for a file with the specified name in a directory and its subdirectories.

    :param filename: Name of the file to search for
    :param search_path: Path to the directory to search in
    :return: List of paths to the files found
    """
    result = []
    
    # Walk through the directory structure recursively
    for dirpath, dirnames, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(dirpath, filename))
    
    return result

# Example usage
if __name__ == '__main__':
    search_directory = '.'  # Change this to the directory you want to search in
    file_to_find = 'example.txt'  # Change this to the file name you're looking for
    found_files = find_file(file_to_find, search_directory)
    if found_files:
        print(f'Found files: {found_files}')
    else:
        print('File not found.')