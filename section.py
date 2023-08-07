import os
import markdown

def read_markdown_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        return file.read()

def convert_markdown_to_html(markdown_content):
    return markdown.markdown(markdown_content)

def edit_html(index,original_html_path,new_article,title):
    try:
        with open(original_html_path, 'r',encoding="utf-8") as file:
            original_content = file.read()
            #markers
            li_marker = "<!-- INSERT_ARTICLE_LIST_HERE -->"
            art_marker = "<!-- INSERT_ARTICLE_HERE  -->"

            new_article_li = f'<li><a href="#" onclick="showContent(\'art{index}\')">{title}</a></li>\n' + li_marker
            
            tag = f'<div class="art" id="art{index}">'
            new_article = tag + new_article + "</div>" + "\n" + art_marker 
            
            result_html = original_content.replace(li_marker,new_article_li)
            result_html = result_html.replace(art_marker,new_article)
            print(">>Added article")
            return result_html
    except: 
        print('>>Error inserting article')

def write_new_hml(html_content, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with open(os.path.join(output_folder, 'index.html'), 'w', encoding='utf-8') as file:
        file.write(html_content)

def add_article(index,filepath,title):
    markdown_article = read_markdown_file(filepath)
    html_article = convert_markdown_to_html(markdown_article)
    original_path ="output/index.html"
    output = "output"
    new_html = edit_html(index,original_path,html_article,title)
    write_new_hml(new_html,output)
