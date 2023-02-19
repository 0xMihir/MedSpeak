from flask import Flask, request
from fhir_handler import PatientFHIR
from ranking import retrieve_rankings_per_string as getRankings
app = Flask(__name__)
from time import sleep
# Path for our main Svelte page

@app.route("/rankings", methods=["POST"])
def rankingList():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return 'Content-Type not supported!'

    if "text" not in request.json:
        # status code 400: bad request
        return {
            "error": "No text provided" 
        }, 400
    text = request.json["text"]

    patient = PatientFHIR("patient3.json")  # TODO: prevent directory traversal
    result = {
        "conditions": {
            "data": patient.conditions,
        },
        "encounters": {
            "data": patient.encounters,
        },
        "medications": {
            "data": patient.medications,
        },
        "observations": {
            "data": patient.observations,
        },
        "procedures": {
            "data": patient.procedures,
        },
        "immunizations": {
            "data": patient.immunizations,
        }
    }
    
    conditions = patient.getConditionList()
    result["conditions"]["rankings"] = getRankings(text, conditions)
    
    encounters = patient.getEncounterList()
    result["encounters"]["rankings"] = getRankings(text, encounters)

    medications = patient.getMedicationList()
    result["medications"]["rankings"] = getRankings(text, medications)

    observations = patient.getObservationList()
    result["observations"]["rankings"] = getRankings(text, observations)

    procedures = patient.getProcedureList()
    result["procedures"]["rankings"] = getRankings(text, procedures)
    
    immunizations = patient.getImmunizationList()
    result["immunizations"]["rankings"] = getRankings(text, immunizations)
    
    return result


if __name__ == "__main__":
    app.run(debug=True)
