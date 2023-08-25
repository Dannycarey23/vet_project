class Pet:
    def __init__(self, name, dob, type, gender, owners_name, owners_phone, treatment_notes, id = None):
        self.name = name
        self.dob = dob
        self.type = type
        self.gender = gender
        self.owners_name = owners_name
        self.owners_phone = owners_phone
        self.treatment_notes = treatment_notes
        self.id = id