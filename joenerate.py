import re

def replace_fill_color(file_path, colors, names):
    with open(file_path, 'r') as file:
        content = file.read()

    pattern = r'fill="#fff000"'

    for color, name in zip(colors, names):
        new_content = re.sub(pattern, f'fill="{color}"', content)
        new_file_name = f'{name}.svg'
        with open(new_file_name, 'w') as new_file:
            new_file.write(new_content)

file_path = 'costume1.svg'
colors = ['#ff0000', '#ff7f00', '#ffff00', '#00ff00', '#0000ff', '#4b0082', '#8b00ff']
names = ["josh", "john", "joe", "tom", "sam", "nick", "paul"]

replace_fill_color(file_path, colors, names)
