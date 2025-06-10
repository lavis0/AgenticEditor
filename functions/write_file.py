import os
from google.genai import types

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    file_path_abs = ''

    if file_path:
        file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))
    if not file_path_abs.startswith(working_dir_abs):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(os.path.dirname(file_path_abs)):
        try:
            os.makedirs(os.path.dirname(file_path_abs))
        except Exception as e:
            return f'Error: e'

    # write to file
    try:
        with open(file_path_abs, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'

schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Writes specified contents to a file at a specified path,"
                    "constrained to the current working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path to the file to write to,"
                                " relative to the working directory.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The contents to write to the file at "
                                "the specified path.",
                ),
            },
        ),
    )