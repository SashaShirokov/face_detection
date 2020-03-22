
import face_recognition
import cv2
import datetime

import generator

from flask import Flask, render_template, make_response, url_for, Response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


date = datetime.date.today()

''' For now we are using dummy data but then we will get it from the video-chat or database. '''
interview_data = [
    {
        'interviewer': 'Epam Mahager',
        'interviewee': 'Firstname Lastname',
        'agenda': 'Data Analyst position',
        'date_time': '{:%B %d, %Y}\n'.format(date),
        'image_source': '/static/default.jpg',
        'video_source': '/static/IMG_0909.MOV'
    }
]


class Home(Resource):
    def get(self):
        return make_response(render_template('home.html', interview_data=interview_data))


class About(Resource):
    def get(self):
        return make_response(render_template('about.html'))


@app.route('/video_feed')
def video_feed():
    return Response(generator.gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


api.add_resource(Home, '/')
api.add_resource(About, '/about')

if __name__ == '__main__':
    app.run(debug=True)
