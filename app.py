import sys


def greet_user(name: str) -> None:
    """Prints a greeting and environment information."""
    print(f"Hello, {name}!")
    print(f"Running on Python version: {sys.version.split()[0]}")


def main():
    # Sample data
    frameworks = ["FastAPI", "NestJS", "Django", "Flask"]

    # Call function
    greet_user("Developer")

    print("\n--- Framework Checklist ---")
    for index, framework in enumerate(frameworks, start=1):
        print(f"{index}. {framework}")


if __name__ == "__main__":
    main()