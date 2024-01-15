from flask import Flask, render_template, request

app = Flask(__name__)

# In-memory storage for simplicity (replace with a database in a real-world application)
appointments = []

@app.route('/')
def index():
    return render_template('index.html', appointments=appointments)

@app.route('/schedule_appointment', methods=['POST'])
def schedule_appointment():
    patient_name = request.form.get('patient_name')
    date = request.form.get('date')
    time = request.form.get('time')

    appointment = {'patient_name': patient_name, 'date': date, 'time': time}
    appointments.append(appointment)

    return render_template('index.html', appointments=appointments, message='Appointment scheduled successfully.')

if __name__ == '__main__':
    app.run(debug=True)