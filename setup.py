from setuptools import setup, find_packages

setup(
    name="cli-todo-usil",
    version="3.2.0",
    description="CLI Todo Diego USIL",
    author="Diego Aguirre",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "todo = todo.cli:main"
        ]
    },
    install_requires=[],
)
