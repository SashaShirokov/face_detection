import datetime


date = datetime.date.today()


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
