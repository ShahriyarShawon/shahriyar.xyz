from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('shayxyz', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

root_dir_files = [
    "index.html",
    "musicILike.html",
    "stuffIUse.html",
    "portfolio.html",
<<<<<<< HEAD
    "donate.html"
=======
    "coolLinks.html"
>>>>>>> 376d946b8224159624c688b1d2e31a7cb21bc570
]

for i in root_dir_files:
    template = env.get_template(i)
    content = template.render()
    f = open(i, "w") 
    f.writelines(content)
    f.close()

guides = [
    "index.html",
    "college_tools.html"
]

for i in guides:
    template = env.get_template("guides/"+i)
    content = template.render()
    f = open("guides/"+i, "w") 
    f.writelines(content)
    f.close()
