import web

render = web.template.render('mvc/controllers/views/')

class Login:
    def GET(self):
        return render.login()

    def POST(self):
        user_data = web.input()
        username = user_data.username
        password = user_data.password

        if username == "gush" and password == "123":
            web.setcookie('username', username)
            return render.index()
