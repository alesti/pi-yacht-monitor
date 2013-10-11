import web
import redis
import os

urls = (
    '/', 'index',
    '/about','about',
    '/webcam','webcam'
)

render = web.template.render('templates', base='layout')


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

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
