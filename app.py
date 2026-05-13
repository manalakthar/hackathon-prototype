from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from datetime import datetime
from modules.nutrilens import analyze_child_photo

app = Flask(__name__)
app.secret_key = 'rozana_secret_key'

# Simulated worker data — in real app this comes from registration
MOCK_WORKER = {
    'name': 'Raju Kumar',
    'profession': 'Construction Worker',
    'phone': '9876543210',
    'language': 'hindi',
    'assigned_day': 'Tuesday',
    'last_checkin': '06 May 2026',
    'last_status': 'safe'
}

@app.route('/')
def home():
    worker = session.get('worker', MOCK_WORKER)
    return render_template('dashboard.html', worker=worker)

@app.route('/checkin')
def checkin():
    worker = session.get('worker', MOCK_WORKER)
    return render_template('checkin.html', worker=worker)

@app.route('/set_language', methods=['POST'])
def set_language():
    data = request.json
    worker = session.get('worker', MOCK_WORKER.copy())
    worker['language'] = data.get('language', 'english')
    session['worker'] = worker
    return jsonify({'status': 'ok'})

@app.route('/submit_checkin', methods=['POST'])
def submit_checkin():
    data = request.json
    symptoms = data.get('symptoms', [])
    work_symptoms = data.get('work_symptoms', [])
    mental_symptoms = data.get('mental_symptoms', [])
    eating = data.get('eating', '')
    water = data.get('water', '')

    # Risk logic
    high_risk = ['persistent_cough', 'weight_loss', 'night_sweats', 'chemical_exposure']
    medium_risk = ['fever', 'fatigue', 'breathlessness', 'heat_exhaustion', 'stress', 'anxiety']

    all_symptoms = symptoms + work_symptoms + mental_symptoms
    high_flags = [s for s in all_symptoms if s in high_risk]
    medium_flags = [s for s in all_symptoms if s in medium_risk]

    poor_eating = eating in ['sometimes', 'no']
    poor_water = water == 'no'

    if high_flags:
        risk_level = "HIGH"
        color = "red"
        clinic = "PHC Mangalore Central — 1.4km — Open 9am to 5pm"
        schemes = ["Ayushman Bharat — Free treatment up to ₹5 lakh", "ESIC — Free medicines and hospitalisation"]
    elif medium_flags or (poor_eating and poor_water):
        risk_level = "MODERATE"
        color = "orange"
        clinic = "PHC Mangalore Central — 1.4km — Open 9am to 5pm"
        schemes = ["Ayushman Bharat — Free treatment up to ₹5 lakh"]
    else:
        risk_level = "SAFE"
        color = "green"
        clinic = None
        schemes = ["PM POSHAN — Free nutritious meals", "Jan Arogya — Free health checkup camps"]

    return jsonify({
        'risk_level': risk_level,
        'color': color,
        'clinic': clinic,
        'schemes': schemes,
        'date': datetime.now().strftime("%d %B %Y"),
        'high_flags': high_flags,
        'medium_flags': medium_flags
    })

@app.route('/nutrilens')
def nutrilens():
    worker = session.get('worker', MOCK_WORKER)
    return render_template('nutrilens.html', worker=worker)

@app.route('/nutrilens/analyze', methods=['POST'])
def nutrilens_analyze():
    age_months = int(request.form.get('age_months', 24))
    # Photo is uploaded but we use mock analysis for this prototype
    result = analyze_child_photo(age_months)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)