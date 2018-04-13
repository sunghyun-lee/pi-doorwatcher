import aiobotocore
from picamera import PiCamera
from sanic import Sanic
from sanic.response import json
import uuid

app = Sanic()
camera = PiCamera()


@app.route('/capture', methods=['POST'])
async def post_handler(request):
    s3_bucket = 'watcha-v2'

    local_save_path = '/var/tmp/'
    remote_save_path = 'images/'

    file_name = "{0}.jpg".format(uuid.uuid4().hex)

    camera.capture(local_save_path + file_name)

    session = aiobotocore.get_session()
    async with session.create_client('s3', region_name='ap-northeast-1') as client:
        data = open(local_save_path + file_name, 'rb')
        resp = await client.put_object(Bucket=s3_bucket, Key=remote_save_path + file_name, Body=data)

    return json({"resp_from_s3": resp}, status=200)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
