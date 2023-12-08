DROP TABLE pets;
DROP TABLE vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    type VARCHAR(255),
    gender VARCHAR(255),
    owners_name VARCHAR(255),
    owners_phone VARCHAR(255),
    treatment_notes VARCHAR(255),
    vet_id INT REFERENCES vets(id)
);