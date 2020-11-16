import web

urls = (
    '/', 'hello'
)
app = web.application(urls, globals())

render = web.template.render('surogou')

class hello:
    def GET(self):
        return render.index('Dima')

    # def POST(self):
    #     pass

if __name__ == "__main__":
    app.run()