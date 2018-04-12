from picamera import PiCamera


if __name__ == "__main__":
    camera = PiCamera()

    camera.capture('/home/pi/src/photo/image.jpg')
