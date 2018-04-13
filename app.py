from picamera import PiCamera
from sanic import Sanic
from sanic.response import json

app = Sanic()
camera = PiCamera()


@app.route('/capture')
async def capture(request):

    camera.capture('/home/pi/src/photo/image.jpg')

    return json({'hello': 'world'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
