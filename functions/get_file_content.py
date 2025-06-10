import os

def get_file_content(working_directory, file_path):
    work_dir_abs = os.path.abspath(working_directory)
    file_path_abs = ''
    if file_path:
        file_path_abs = os.path.abspath(os.path.join(work_dir_abs, file_path))
    if not file_path_abs.startswith(work_dir_abs):
        return f'Error: Cannot read "{file_path_abs}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path_abs):
        return f'Error: File not found or is not a regular file: "{file_path_abs}"'

    # read file content
    MAX_CHARS = 10000 # to avoid using too many tokens

    try:
        with open(file_path_abs, 'r') as f:
            file_content_str = f.read(MAX_CHARS)
            if len(file_content_str) == MAX_CHARS:
                file_content_str += '[...File "{file_path}" truncated at 10000 characters]'
            return file_content_str
    except Exception as e:
        return f'Error: {e}'
