DROP TABLE pets;
DROP TABLE vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    pet_id INT REFERENCES pets(id)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    type VARCHAR(255),
    gender VARCHAR(255),
    owners_name VARCHAR(255),
    owners_phone INT,
    treatment_notes VARCHAR(255)
);