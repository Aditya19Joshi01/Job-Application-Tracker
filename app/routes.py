from flask import Blueprint, request, jsonify, render_template
from .models import JobApplication
from . import db

api_v1 = Blueprint('api_v1', __name__)

@api_v1.route('/')
def index():
    return render_template('index.html')

# Route to add a new job application
@api_v1.route('/jobs', methods=['POST'])
def add_job():
    data = request.json
    new_job = JobApplication(
        company=data['company'],
        position=data['position'],
        status=data.get('status', 'Applied')
    )
    db.session.add(new_job)
    db.session.commit()
    return jsonify({'message': 'Job added successfully'}), 201


# Route to get all job applications
@api_v1.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = JobApplication.query.all()

    return jsonify([{
        'company': job.company,
        'position': job.position,
        'status': job.status,
        'date_applied': job.date_applied,
        'notes': job.notes
    } for job in jobs])
