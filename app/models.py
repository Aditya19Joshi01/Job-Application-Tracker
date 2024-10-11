from datetime import datetime
from . import db

class JobApplication(db.Model):
    __tablename__ = 'job_applications'
    
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='Applied')  # Status of the application (e.g., Applied, Interviewing)
    date_applied = db.Column(db.DateTime, default=datetime.utcnow)  # Auto-populates with the current date
    notes = db.Column(db.Text, nullable=True)  # Additional notes about the job application
