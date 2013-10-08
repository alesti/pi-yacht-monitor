import web
import redis

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        ret = "<table border='1' cellspacing='0' cellpadding='3'>"
        ret += "<tr><td>Voltage</td><td>" + r.get("boat.voltage") + "</td></tr>"
        ret += "<tr><td>Temperature</td><td>" + r.get("boat.temperature") + "</td></tr>"
        ret += "<tr><td>Bilge</td><td>" + r.get("boat.bilge") + "</td></tr>"
        ret += "</table>"
        return ret

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
