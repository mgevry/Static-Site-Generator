import os
from markdown_blocks import markdown_to_html_node
from pathlib import Path

def extract_title(markdown):
    blocks = markdown.split(sep="\n")
    for block in blocks:
        if block.startswith("#"):
            block = block.strip()
            block = block[2:]
            return block
    raise ValueError("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    file = open(from_path, mode='r')
    file_content = file.read()
    template_file = open(template_path, mode='r')
    template_file_content = template_file.read()
    html_node = markdown_to_html_node(file_content)
    html_string = html_node.to_html()
    title = extract_title(file_content)
    template_file_content = template_file_content.replace("{{ Title }}", title)
    final_content = template_file_content.replace("{{ Content }}", html_string)
    dest_path_directory = os.path.dirname(dest_path)
    os.makedirs(dest_path_directory, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(final_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_list = os.listdir(dir_path_content)
    for entry in content_list:
        from_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
            
            
    
