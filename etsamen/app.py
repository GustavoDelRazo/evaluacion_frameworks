import web

urls = (
    '/', 'mvc.controllers.login.Login',
    '/index', 'mvc.controllers.index.Index',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
