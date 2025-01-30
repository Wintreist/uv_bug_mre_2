from pathlib import Path

directory = Path(__file__).parent
for lib_index in range(1, 10):
    lib_path = directory.joinpath(f"test_lib_{lib_index}")
    lib_path.mkdir(parents=True, exist_ok=True)

    with open(lib_path.joinpath("__init__.py"), "w") as f:
        f.write(f'def hello() -> str:\n    return "Hello from test-lib-{lib_index}!"\n')
