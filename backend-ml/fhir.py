from fhir.resources.bundle import Bundle
from fhir.resources.patient import Patient
from fhir.resources.condition import Condition
from fhir.resources.observation import Observation
from fhir.resources.medicationrequest import MedicationRequest
from fhir.resources.procedure import Procedure
from fhir.resources.encounter import Encounter
from fhir.resources.immunization import Immunization


class PatientFHIR:
    def __init__(self, file) -> None:
        self.file = file
        self.bundle = Bundle.parse_file(self.file)
        resources = []
        if self.bundle.entry is not None:
            for entry in self.bundle.entry:
                resources.append(entry.resource)

        patientData = Patient.parse_obj(resources[0])
        self.gender = patientData.gender
        self.birthDate = patientData.birthDate
        name = patientData.name[0]
        self.name = name.given[0] + " " + name.family
        self.id = patientData.id

        self.conditions = {}
        self.encounters = {}
        self.immunizations = {}
        self.medications = {}
        self.procedures = {}
        self.observations = {}

        for resource in resources:
            if type(resource) == Condition:
                if resource.code.text in self.conditions:
                    self.conditions[resource.code.text].append(resource)
                else:
                    self.conditions[resource.code.text] = [resource]
            elif type(resource) == Encounter:
                if resource.type[0].text in self.encounters:
                    self.encounters[resource.type[0].text].append(resource)
                else:
                    self.encounters[resource.type[0].text] = [resource]
            elif type(resource) == Immunization:
                if resource.vaccineCode.text in self.immunizations:
                    self.immunizations[resource.vaccineCode.text].append(
                        resource)
                else:
                    self.immunizations[resource.vaccineCode.text] = [resource]
            elif type(resource) == MedicationRequest:
                if resource.medicationCodeableConcept.text in self.medications:
                    self.medications[resource.medicationCodeableConcept.text].append(
                        resource)
                else:
                    self.medications[resource.medicationCodeableConcept.text] = [
                        resource]
            elif type(resource) == Procedure:
                if resource.code.text in self.procedures:
                    self.procedures[resource.code.text].append(resource)
                else:
                    self.procedures[resource.code.text] = [resource]
            elif type(resource) == Observation:
                if resource.code.text in self.observations:
                    self.observations[resource.code.text].append(resource)
                else:
                    self.observations[resource.code.text] = [resource]

    def getConditionList(self):
        return self.conditions.keys()

    def getEncounterList(self):
        return self.encounters.keys()

    def getImmunizationList(self):
        return self.immunizations.keys()

    def getMedicationList(self):
        return self.medications.keys()

    def getProcedureList(self):
        return self.procedures.keys()

    def getObservationList(self):
        return self.observations.keys()

    def getCondition(self, condition):
        return self.conditions[condition]

    def getEncounter(self, encounter):
        return self.encounters[encounter]

    def getImmunization(self, immunization):
        return self.immunizations[immunization]

    def getMedication(self, medication):
        return self.medications[medication]

    def getProcedure(self, procedure):
        return self.procedures[procedure]

    def getObservation(self, observation):
        return self.observations[observation]

    def getGender(self):
        return self.gender

    def getName(self):
        return self.name

    def getBirthDate(self):
        return self.birthDate
