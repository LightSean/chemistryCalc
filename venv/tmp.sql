(1)

CREATE TABLE Enrolled (
    sid INTEGER,
    cid INTEGER,    
    FOREIGN KEY (sid) REFERENCES Student(sid) ON DELETE CASCADE,
    FOREIGN KEY (cid) REFERENCES Course(cid) ON DELETE CASCADE
);

(2)

INSERT INTO Student VALUES (
    100, 'Sean', 1800
);
INSERT INTO Student VALUES (
    101, 'Inbal', 1800
);



(3)

UPDATE Enrolled 
SET cid = 236363
WHERE cid = 236341

(4)


CREATE TABLE MAMAN AS 
    SELECT sid 
    FROM Enrolled
    WHERE cid = 236363




