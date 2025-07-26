-- Create Patient Table --

CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(45),
    vaccin_status VARCHAR(45),
    medical_problems TEXT,
    insurance VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Create Prescription Table --

CREATE TABLE prescriptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address TEXT,
    medicines TEXT,
    directions TEXT,
    refill TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- SP: Add new patient --

CREATE DEFINER=`root`@`localhost` PROCEDURE `add_patient`(
    IN name VARCHAR(255),
    IN phone VARCHAR(50),
    IN vaccin_status VARCHAR(50),
    IN medical_problems TEXT,
    IN insurance VARCHAR(255)
)
BEGIN
    INSERT INTO medextract.patients (name, phone, vaccin_status, medical_problems, insurance)
    VALUES (name, phone, vaccin_status, medical_problems, insurance);
END


-- SP: Add new prescription --

CREATE DEFINER=`root`@`localhost` PROCEDURE `add_prescription`(
    IN name VARCHAR(255),
    IN address TEXT,
    IN medicines TEXT,
    IN directions TEXT,
    IN refill TEXT
)
BEGIN
    INSERT INTO medextract.prescriptions (name, address, medicines, directions, refill)
    VALUES (name, address, medicines, directions, refill);
END