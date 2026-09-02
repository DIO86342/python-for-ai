select version();
CREATE TABLE names(
    fname VARCHAR(120),
    lasnme VARCHAR(120)
);



INSERT INTO names(fname, lasnme)
VALUES ('Abdikani', 'hassan');
SELECT *FROM names;
SELECT *FROM cars;


INSERT INTO cars (brand, model, year, color)
VALUES ('Toyota', 'Corolla', 2020, 'Blue');

SELECT * FROM cars;