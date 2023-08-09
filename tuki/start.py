import os 
import shutil
from . import genFunc as gp

CONFIG_FILE = "config.json"


def copy_files(source_folder, destination_folder):
    try:
        # Verifica si la carpeta de destino existe, si no, créala
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        # Lista todos los archivos en la carpeta de origen
        files = os.listdir(source_folder)
        for file in files:
            # Construye las rutas completas de origen y destino para cada archivo
            source_file = os.path.join(source_folder, file)
            destination_file = os.path.join(destination_folder, file)
            # Copia el archivo de origen al destino
            shutil.copy2(source_file, destination_file)
        print(">>Copying template files")
    except Exception as e:
        print(f"Error copying files: {e}")

def insert_html_into_html(original_html, insert_html,title):
    try:
        with open(original_html, 'r', encoding='utf-8') as file1:
            original_content = file1.read()
        marker = '<!-- INSERT_CONTENT_HERE -->'
        title_marker = '<!--Title -->'
        result_html = original_content.replace(marker, insert_html)
        result_html = result_html.replace(title_marker,title)
        print(">>Succesful insert")
        return result_html
    except: print(">>Error inserting content into template")

def generate_static_website(html_content, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(os.path.join(output_folder, 'index.html'), 'w', encoding='utf-8') as file:
        file.write(html_content)

def init(input_file,title):
    #some folder declarations
    conf = gp.loadConf(CONFIG_FILE)
    template_folder = conf['template_folder']
    output_folder = conf['output_folder']
    template = template_folder + '/index.html'

    #copy template files
    copy_files(template_folder,output_folder)
    #initialize site
    markdown_content = gp.read_markdown_file(input_file)
    html_content = gp.convert_markdown_to_html(markdown_content)
    final_html = insert_html_into_html(template,html_content,title)
    generate_static_website(final_html, output_folder)
    print(">>init complete, tuki")

