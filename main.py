import streamlit as st
import requests
from PIL import Image
from PIL import ImageDraw, ImageFont
import math
import io
#import json

st.title('顔認識アプリ')

subscription_key ='19fc85f0a944448292a791aa4ee5f6d9'
# with open('secret.json') as f:
#     secret_json = json.load(f)
# subscription_key = secret_json['subscription_key']
assert subscription_key #判定する時に使う(変数に文字列が入っているか確かめる)
face_api_url ='https://20201129sota.cognitiveservices.azure.com/face/v1.0/detect'

upload_file = st.file_uploader('Choose an image...', type=None)

if upload_file is not None:
  img = Image.open(upload_file)
  #画像をバイナリデータで取り出す
  with io.BytesIO() as output:
      img.save(output, format='JPEG')
      binary_img = output.getvalue() #バイナリデータの取得
      
  #urlではなく、ローカルから画像を読み込むからheaderに1つ付け加える。content-typeが通常URLがベースだがstream(画像)を送りますよということ
  headers = {
      'Content-Type': 'application/octet-stream',
      'Ocp-Apim-Subscription-Key': subscription_key}

  params = {
      'returnFaceId': 'true',
      'returnFaceAttributes':'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
  }

  #requests.postでPostリクエストで送りますよということ
  res = requests.post(face_api_url, params=params,
                          headers=headers, data=binary_img)
  results = res.json()
  font = ImageFont.truetype("arial.ttf", 32)
  for result in results:
      rect = result['faceRectangle']
      gender = result['faceAttributes']['gender']
      old = math.floor(result['faceAttributes']['age'])
      draw = ImageDraw.Draw(img)
      draw.rectangle([(rect['left'], rect['top']), (rect['left']+rect['width'], rect['top']+rect['height'])], fill=None, outline='red', width=6)
      draw.text((rect['left'], rect['top']-150), gender+', old:'+str(old),font=font, fill='white')
  st.image(img, caption='Uploaded Image', use_column_width=True) #Trueにすると幅を自動補正してくれる

  #変更しました2

