import os
import markdown

def replaceBetween(mark1,mark2,text,new_text):
    begin = text.find(mark1)
    end = text.find(mark2)
    
    if begin != -1 and end != -1 and begin < end:
        delete_content = text[begin + len(mark1):end]
        modified_text = text.replace(delete_content, new_text)
        return modified_text
    else:
        return text


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

            section_start = f'<!-- START_OF_SECTION_{index}-->'
            section_end = f'<!--END_OF_SECTION_{index}-->'
            
            li_index_start = f'<!--LI_FOR_{index}-->'
            li_index_end = f'<!--END_OF_LI_FOR_{index}-->'

            new_article_li = f'<li><a href="#" onclick="showContent(\'art{index}\')">{title}</a></li>\n'
             
            tag = f'<div class="art" id="art{index}">'
            new_article = tag + new_article + "</div>" + "\n" 
            #if section already exists, modify it
            if section_start in original_content and li_index_start in original_content:
                result_html = replaceBetween(li_index_start,li_index_end,original_content,new_article_li)
                result_html = replaceBetween(section_start,section_end,result_html,new_article) 
                print(f'>>Modified article {index}')
            #else create new one
            else:
                new_article = section_start +'\n'+ new_article +'\n'+section_end + '\n' +art_marker + '\n'
                new_article_li = li_index_start +' \n' + new_article_li +'\n'+ li_index_end + '\n' + li_marker + '\n'
                result_html = original_content.replace(li_marker,new_article_li)
                result_html = result_html.replace(art_marker,new_article)
                print(">>Added new article")
            print(">>tuki")
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
    original_path ="../output/index.html"
    output = "../output"
    new_html = edit_html(index,original_path,html_article,title)
    write_new_hml(new_html,output)
