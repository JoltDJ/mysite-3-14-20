from jinja2 import Template

def welcomeHTML():
    with open('welcome.html') as f:
        s = f.read()
    return s

def main():
    user1 = { 'name': 'Alice', 'likes': 123}
    user2 = { 'name': 'Jimmy', 'likes': 1234}

    tmpl = Template(welcomeHTML())

    print(tmpl.render({ 'user': user1}))
    print(tmpl.render({ 'user': user2}))

main()