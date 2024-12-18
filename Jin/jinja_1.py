from jinja2 import Template

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

per = Person("Фёдор", "33")
tm = Template("Привет, меня зовут {{p.name}}, и мне {{p.age}} лет")
msg = tm.render(p=per)

print(msg)
