import web
import redis

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        voltage = "xxx" if r.get("boat.voltage") is None else r.get("boat.voltage") 
        temperature = "xxx" if r.get("boat.temperature") is None else r.get("boat.temperature")
        bilge = "xxx" if r.get("boat.bilge") is None else r.get("boat.bilge")
        ret = "<table border='1' cellspacing='0' cellpadding='3'>"
        ret += "<tr><td>Voltage</td><td>" + voltage + "</td></tr>"
        ret += "<tr><td>Temperature</td><td>" + temperature + "</td></tr>"
        ret += "<tr><td>Bilge</td><td>" + bilge + "</td></tr>"
        ret += "</table>"
        return ret

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
