import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())
render = web.template.render('C:/Users/Владелец/wezom-python-course/students/Vladimir/h_w/7/templatemo_529_ramayana')
name = 'Vladimir'
class hello:
    def GET(self, name):
        return render.index('name')

if __name__ == "__main__":
    app.run()