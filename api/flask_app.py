from flask import Flask, render_template, make_response, url_for
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


''' For now we are using dummy data but then we will get it from the video-chat or database. '''
interview_data = [
    {
        'interviewer': 'Epam Mahager',
        'interviewee': 'First Candidate',
        'agenda': 'Data Analyst position',
        'date_time': 'March 18, 2020',
        'image_source': '/static/avatar.jpg'
    }
]


class Home(Resource):
    def get(self):
        return make_response(render_template('home.html', interview_data=interview_data))


class About(Resource):
    def get(self):
        return make_response(render_template('about.html'))


api.add_resource(Home, '/')
api.add_resource(About, '/about')


if __name__ == '__main__':
    app.run(debug=True)
