import boto3

from picamera import PiCamera
from time import sleep

client = boto3.client('s3', region_name='<ap-southeast-2>', aws_access_key_id='<AWS Access Key ID>', aws_secret_access_key='<AWS SECRET ACCESS KEY>')

while True:
    sleep(5)
    camera = PiCamera()
    camera.capture('/home/pi/Desktop/beerfridge.jpg')
    client.upload_file('/home/pi/Desktop/beerfridge.jpg', 'codefest-beerly', 'beerfridge.jpg', ExtraArgs={'ACL':'public-read'})
    camera.close()
    sleep(30)