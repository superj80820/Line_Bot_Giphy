from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, VideoSendMessage
)
import requests
import json
import moviepy.editor as mp
import os
import random, string

app = Flask(__name__)
FileRoute='%s' %os.path.dirname(os.path.abspath(__file__))

line_bot_api = LineBotApi('vxJfXmnKPVhcOp7rQipUTabXQp/Zc227v0dRT0Am+a4pl/nr6hUDLRsJGoe8aY8/1MW4sqyo+NQ7+WkAH+Madtn4DlYvzaKOqSQE+uSCtmHIPLTdguf3UVjyQ8XJdiLg8Otg2imHALz2mdhXYU8yYwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0ef7975dd3724126dec33c34af95d46a')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text[0] == '/' or event.message.text[0] == '／':
        name = ''.join(random.choice(string.ascii_letters) for x in range(10))

        resp = requests.get("http://api.giphy.com/v1/gifs/random?api_key=V5pYPSB0TKF00sZUnt7feN8cjbikI1UF&tag=%s" %(event.message.text))
        resp_json = resp.json()
        get_source_gif = resp_json['data']['images']['fixed_height_still']['url']
        git_source_video = resp_json['data']['images']['fixed_width']['mp4']
#        with open('%s/data/gif/%s.gif' %(FileRoute, name), 'wb') as f:
#            f.write(requests.get(git_source).content)
#        clip = mp.VideoFileClip("%s/data/gif/%s.gif" %(FileRoute, name))
#        clip.write_videofile("%s/data/mp4/%s.mp4" %(FileRoute, name))
        video_message = VideoSendMessage(
            original_content_url=get_source_video,
            preview_image_url=git_source_gif
        )
        line_bot_api.reply_message(
            event.reply_token,video_message)

if __name__ == "__main__":
    app.run()
