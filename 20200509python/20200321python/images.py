from jinja2 import Template

def itemsHTML():
    with open('images.html') as f:
        s = f.read()
    return s

def main():
    image_list = [
        {'title': 'Pickle Rick',
         'url': 'https://images-na.ssl-images-amazon.com/images/I/41rqwE%2BbbjL._SX331_BO1,204,203,200_.jpg',
         'desc': 'Some description ...'
         },
        {'title': 'Rubix Cube',
         'url': 'https://i.pinimg.com/originals/b5/5e/3b/b55e3bafe484a0ead34d5e3849bd1e11.gif',
         'desc': 'Some description ...'
         },
         {'title': 'Mrbeast',
         'url': 'https://pbs.twimg.com/profile_images/994592419705274369/RLplF55e_400x400.jpg',
         'desc': 'Some description ...'
         },
    ]
    tmpl = Template(itemsHTML())
    print(tmpl.render({'images' : image_list}))

main()