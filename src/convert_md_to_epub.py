import markdown
import ebooklib
from ebooklib import epub
import argparse

def markdown_to_html(markdown_text):
    """ Convert Markdown text to HTML """
    html = markdown.markdown(markdown_text)
    return html

def create_epub(html_content, output_file, title, author):
    """ Create an EPUB file from HTML content """
    book = epub.EpubBook()

    # Set the title and author
    book.set_title(title)
    book.set_language('en')
    book.add_author(author)

    # Create a chapter
    c1 = epub.EpubHtml(title='Chapter 1', file_name='chap_01.xhtml', lang='en')
    c1.content = html_content

    # Add chapter to the book
    book.add_item(c1)

    # Define Table Of Contents
    book.toc = (epub.Link('chap_01.xhtml', 'Chapter 1', 'id1'), )

    # Add default NCX and Cover
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Define CSS style
    style = 'BODY {color: white;}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)

    # Set spine
    book.spine = ['nav', c1]

    # Write to the file
    epub.write_epub(output_file, book, {})

def main():
    parser = argparse.ArgumentParser(description="Convert a Markdown file to an EPUB book.")
    parser.add_argument("markdown_file", type=str, help="Path to the Markdown file to convert.")
    parser.add_argument("-o", "--output", type=str, default="output.epub", help="Output EPUB file name (default is 'output.epub').")
    parser.add_argument("-t", "--title", type=str, default="Sample Book", help="Title of the book (default is 'Sample Book').")
    parser.add_argument("-a", "--author", type=str, default="Anonymous", help="Author of the book (default is 'Anonymous').")

    args = parser.parse_args()
    markdown_file_path = args.markdown_file
    output_file = args.output
    title = args.title
    author = args.author

    with open(markdown_file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    html_content = markdown_to_html(markdown_text)
    create_epub(html_content, output_file, title, author)
    print(f"EPUB file '{output_file}' has been created successfully.")

if __name__ == "__main__":
    main()
