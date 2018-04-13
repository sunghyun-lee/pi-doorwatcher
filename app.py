# from picamera import PiCamera
from sanic import Sanic
from sanic.response import json
import uuid

app = Sanic()
camera = PiCamera()


@app.route('/capture')
async def capture(request):
    local_save_path = '/var/tmp/'
    file_name = "{0}.jpg".format(uuid.uuid4().hex)

    camera.capture(local_save_path + file_name)

    return json({'hello': 'world'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
