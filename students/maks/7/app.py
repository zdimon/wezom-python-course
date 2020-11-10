import web

render = web.template.render('web')

urls = (
    '/(.*)', 'index'
)

class index:
    def GET(self, name):
        name = "Joe"
        return render.index(name)
        #i = web.input(name=None)
        #return render.index(i.name)
    #def GET1(self, da):
        #u = web.input(da=None)
        #return render.index(u.da)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()