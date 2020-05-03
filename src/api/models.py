from api import db
import datetime
from api.config import Config


date = datetime.date.today()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"User('{self.username}', '{self.image_file}')"


''' For now we are using dummy data but then we will get it from the video-chat or database. '''
interview_data = [
    {
        'interviewer': 'Epam Manager',
        'interviewee': 'Firstname Lastname',
        'agenda': 'Data Analyst position',
        'date_time': '{:%B %d, %Y}\n'.format(date),
        'image_source': '/static/default.jpg',
        'video_source': '/static/IMG_0909.MOV'
    }
]
