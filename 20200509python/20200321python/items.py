from jinja2 import Template

def itemsHTML():
    with open('items.html') as f:
        s = f.read()
    return s

def main():
    item_list = [
        {'name': 'apple', 'count': 100},
        {'name': 'guava', 'count': 75},
        {'name': 'banana', 'count': 30}
    ]
    tmpl = Template(itemsHTML())
    print(tmpl.render({'items' : item_list}))

main()