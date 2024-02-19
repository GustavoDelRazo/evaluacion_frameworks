import web

render = web.template.render('mvc/controllers/views/')

class Index:
    def GET(self):
        return render.index()
