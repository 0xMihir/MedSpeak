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
                condition = {
                    # "name": resource.code.text,
                    "date": resource.onsetDateTime,
                }
                if resource.code.text in self.conditions:
                    self.conditions[resource.code.text].append(condition)
                else:
                    self.conditions[resource.code.text] = [condition]
            elif type(resource) == Encounter:
                encounter = {
                    # "name": resource.type[0].text,
                    "date": resource.period.start,
                    # "location": resource.location[0].location.display,
                    # "reason": resource.reasonCode[0].text,
                }

                if resource.type[0].text in self.encounters:
                    self.encounters[resource.type[0].text].append(encounter)
                else:
                    self.encounters[resource.type[0].text] = [encounter]
            elif type(resource) == Immunization:
                immunization = { 
                    # "name": resource.vaccineCode.text,
                    "date": resource.occurrenceDateTime,
                }

                if resource.vaccineCode.text in self.immunizations:
                    self.immunizations[resource.vaccineCode.text].append(
                        immunization)
                else:
                    self.immunizations[resource.vaccineCode.text] = [immunization]
            elif type(resource) == MedicationRequest:
                medication = {
                    # "name": resource.medicationCodeableConcept.text,
                    "date": resource.authoredOn,
                }

                # if resource.dosageInstruction[0]: 
                    # medication["dosage"] = resource.dosageInstruction[0].doseAndRate[0].doseQuantity.value
                    # medication["unit"] = resource.dosageInstruction[0].doseAndRate[0].doseQuantity.unit

                if resource.medicationCodeableConcept.text in self.medications:
                    self.medications[resource.medicationCodeableConcept.text].append(
                        medication)
                else:
                    self.medications[resource.medicationCodeableConcept.text] = [
                        medication]
            elif type(resource) == Procedure:
                procedure = {
                    # "name": resource.code.text,
                    "date": resource.performedPeriod.start,
                }
                if resource.code.text in self.procedures:
                    self.procedures[resource.code.text].append(procedure)
                else:
                    self.procedures[resource.code.text] = [procedure]
            elif type(resource) == Observation:
                observation = {
                    # "name": resource.code.text,
                    "date": resource.effectiveDateTime,
                }

                if resource.valueQuantity:
                    observation["value"] = resource.valueQuantity.value
                    observation["unit"] = resource.valueQuantity.unit

                if resource.component:
                    observation["components"] = []
                    for component in resource.component:
                        observation["components"].append({
                            "name": component.code.text,
                            "value": component.valueQuantity.value,
                            "unit": component.valueQuantity.unit,
                        })

                if resource.code.text in self.observations:
                    self.observations[resource.code.text].append(observation)
                else:
                    self.observations[resource.code.text] = [observation]

    def getConditionList(self):
        return list(self.conditions.keys())

    def getEncounterList(self):
        return list(self.encounters.keys())

    def getImmunizationList(self):
        return list(self.immunizations.keys())

    def getMedicationList(self):
        return list(self.medications.keys())

    def getProcedureList(self):
        return list(self.procedures.keys())

    def getObservationList(self):
        return list(self.observations.keys())

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
