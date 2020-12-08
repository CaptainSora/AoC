def initialize(year, day):
    with open(f"{year}/day{day:02}.py", "w") as f:
        f.write(
            f"def day{day:02}a():\n"
            f'\twith open("{year}/day{day:02}_input.txt", "r") as f:\n'
            f'\t\tpass\n\n'
            f"def day{day:02}b():\n"
            f'\twith open("{year}/day{day:02}_input.txt", "r") as f:\n'
            f'\t\tpass\n\n'
            f'print(day{day:02}a())\n'
        )
