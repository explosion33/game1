from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name='Pong',
    author = 'Ethan Armstrong',
    options={
        "build_exe": {
            "packages":["pygame", "sys", "random"],
            "include_files":["settings.txt"]
            }},
    executables = executables,
    version = "5.1.1"
)