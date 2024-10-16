def run(html: str) -> str:
    tag = '#'
    tag_number = int(html[2])
    total_hashtags = tag * tag_number
    lef_headline_symbol = html.find('>')
    new_html = html[lef_headline_symbol + 1 :]
    right_headline_symbol = new_html.find('<')
    right_headline = new_html[right_headline_symbol:]
    markdown = new_html.replace(right_headline, '')
    markdown = f'{total_hashtags} {markdown}'
    return markdown


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
