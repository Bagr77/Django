from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page.htm')
msg = tm.render(domain='http://proproprogs.ru', title="Про Jinja")

print(msg)