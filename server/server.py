import web
import redis
import os
from web import form
import datetime

urls = (
    '/', 'index',
    '/about','about',
    '/webcam','webcam',
    '/config','config',
    '/collectors','collectors'
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
        boatkeys = r.keys("boat.*")
        rows = []
        for boatkey in boatkeys:
            row = r.hgetall(boatkey)
            row["key"] = boatkey.split(".")[1]
            row["timestamp"]  = datetime.datetime.fromtimestamp(int(row["time"])).strftime('%Y-%m-%d %H:%M:%S')
            rows.append(row)
            print row
        print rows
        return render.index(rows)

class webcam:
    def GET(self):
        os.system("fswebcam -r 800x600 -d /dev/video0 ./static/webcam/webcam.jpg")
        return render.webcam("static/webcam/webcam.jpg")

class collectors:
    def GET(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        collectors = []
        collkeys = r.keys("collector.*")
        for collkey in collkeys:
            row = r.hgetall(collkey)
            row["key"] = collkey.split(".")[1]
            collectors.append(row)
        return render.collectors(collectors)

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
