import os
from google.genai import types

# returns strings so LLM can handle errors
def get_files_info(working_directory, directory=None):
    # correct to absolute paths, working dir
    working_dir_abs = os.path.abspath(working_directory)
    target_dir_abs = working_dir_abs

    if directory:
        target_dir_abs = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir_abs.startswith(working_dir_abs):
        return f'Error: Cannot list "{target_dir_abs}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir_abs):
        return f'Error: "{target_dir_abs}" is not a directory'

    output = ''

    for filename in os.listdir(target_dir_abs):
        filepath = os.path.join(target_dir_abs, filename)
        try:
            file_size = os.path.getsize(filepath)
        except OSError as e:
            return f'Error: getsize failed for {filename} as "{e}"'
        is_dir = os.path.isdir(filepath)
        output += f'- {filename}: file_size:{file_size} bytes, is_dir={is_dir}\n'

    return output

schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes,"
                    "constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory."
                                "If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )