import requests


url = "https://s3.amazonaws.com/download.onnx/models/opset_9/inception_v1.tar.gz"

response = requests.get(url)
with open('output', 'wb') as file:
    file.write(response.content)
