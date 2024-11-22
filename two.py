import csv
from flask import Flask, request, jsonify

app = Flask(__name__)

# # Sample CSV data
# data = [
#     ['Student_ID', 'Attendance_percentage', 'CGPA'],
#     ['23BCE0275', '85', '9.5'],
#     ['23BCE0276', '70', '8.0'],
#     ['23BCE0277', '90', '9.0'],
#     ['23BCE0278', '65', '7.5'],
# ]

students = {}
with open('students.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

with open('students.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students[row['Student_ID']] = {
            'Attendance_percentage': float(row['Attendance_percentage']),
            'CGPA': float(row['CGPA'])
        }

# Prolog rules (simulated in Python)
def eligible_for_scholarship(student_id):
    student = students.get(student_id)
    if student and student['Attendance_percentage'] >= 75 and student['CGPA'] >= 9.0:
        return True
    return False

def permitted_for_exam(student_id):
    student = students.get(student_id)
    if student and student['Attendance_percentage'] >= 75:
        return True
    return False

# REST API endpoints
@app.route('/scholarship/<student_id>')
def check_scholarship(student_id):
    if student_id not in students:
        return jsonify({'error': 'Student ID not found'}), 404
    status = 'Eligible' if eligible_for_scholarship(student_id) else 'Not Eligible'
    return jsonify({'status': status}), 200

@app.route('/exam/<student_id>')
def check_exam_permission(student_id):
    if student_id not in students:
        return jsonify({'error': 'Student ID not found'}), 404
    status = 'Permitted' if permitted_for_exam(student_id) else 'Not Permitted'
    return jsonify({'status': status}), 200

@app.route('/eligibility/<student_id>')
def check_eligibility(student_id):
    if student_id not in students:
        return jsonify({'error': 'Student ID not found'}), 404
    scholarship_status = eligible_for_scholarship(student_id)
    exam_status = permitted_for_exam(student_id)
    return jsonify({
        'scholarship_status': 'Eligible' if scholarship_status else 'Not Eligible',
        'exam_status': 'Permitted' if exam_status else 'Not Permitted'
    }), 200

if __name__ == '__main__':
    app.run(debug=True)