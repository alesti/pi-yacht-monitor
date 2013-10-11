import web
import redis
import os
from web import form

urls = (
    '/', 'index',
    '/about','about',
    '/webcam','webcam',
    '/config','config'
)

render = web.template.render('templates', base='layout')


def get_nameform(boatname):
    return form.Form(form.Textbox("name",description="Name",value=boatname),form.Button("speichern", type="submit", description="Speichern"))


class about:
    def GET(self):
        return render.about()


class index:
    def GET(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        voltage = "xxx" if r.get("boat.voltage") is None else r.get("boat.voltage") 
        temperature = "xxx" if r.get("boat.temperature") is None else r.get("boat.temperature")
        bilge = "xxx" if r.get("boat.bilge") is None else r.get("boat.bilge")
        return render.index(voltage,temperature,bilge)

class webcam:
    def GET(self):
        os.system("fswebcam -r 800x600 -d /dev/video0 ./static/webcam/webcam.jpg")
        return render.webcam("static/webcam/webcam.jpg")

class config:

    def GET(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        boatname = r.get("config.boat.name")
        return render.config(get_nameform(boatname))
    def POST(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        i = web.input()
        print i
        boatname=i.name
        r.set("config.boat.name",boatname) 
        return render.config(get_nameform(boatname))

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
