import web
import redis

urls = (
    '/', 'index',
    '/about','about'
)

class about:
    def GET(self):
        render = web.template.render('templates', base='layout')
        return render.about()


class index:
    def GET(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        voltage = "xxx" if r.get("boat.voltage") is None else r.get("boat.voltage") 
        temperature = "xxx" if r.get("boat.temperature") is None else r.get("boat.temperature")
        bilge = "xxx" if r.get("boat.bilge") is None else r.get("boat.bilge")
        render = web.template.render('templates', base='layout')
        return render.index(voltage,temperature,bilge)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
