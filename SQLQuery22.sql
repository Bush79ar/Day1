CREATE TABLE COLLEGE
(Cl_Code CHAR(3) PRIMARY KEY,
Cl_Name VARCHAR(40) NOT NULL,
Cl_Dean VARCHAR(40),
);

CREATE TABLE DEPARTMENT (
    Dp_Code CHAR(4) PRIMARY KEY,
    Dp_Name VARCHAR(40) NOT NULL,
    Dp_HoD VARCHAR(30),
    Dp_Col CHAR(3),
    CONSTRAINT FK_DEPARTMENT_College
    FOREIGN KEY (Dp_Col)
    REFERENCES COLLEGE(Cl_Code)
);

CREATE TABLE BOOK (
    Bk_ID NUMERIC(6, 0) PRIMARY KEY,
    Bk_Title VARCHAR(50) NOT NULL,
    Bk_Edition NUMERIC(2, 0),
    Bk_#ofPages NUMERIC(4, 0) CHECK (Bk_#ofPages > 0),
    Bk_TotalCopies NUMERIC(5, 0),
    Bk_RemCopies NUMERIC(5, 0)
);

CREATE TABLE BOOKTOPIC
(Tp_Desc NUMERIC(6,0) PRIMARY KEY,
Tp_BkID VARCHAR(30) NOT NULL,
);

CREATE TABLE BORROWER (
    Br_ID NUMERIC(6, 0) PRIMARY KEY,
    Br_Name VARCHAR(30) NOT NULL,
    Br_Dept CHAR(4),
    Br_Mobile CHAR(8) CHECK (Br_Mobile >= '90000000'),
    Br_City VARCHAR(20),
    Br_House# CHAR(4),
    Br_Type CHAR(1) CHECK (Br_Type IN ('S', 'E')),
    CONSTRAINT FK_BORROWER_DEPARTMENT
    FOREIGN KEY (Br_Dept)
    REFERENCES DEPARTMENT(Dp_Code)
);



CREATE TABLE EMPLOYEE (
    Em_ID NUMERIC(6, 0) PRIMARY KEY CHECK (Em_ID > 0),
    Em_Office# CHAR(4) NOT NULL,
    Em_Ext# NUMERIC(4) CHECK (Em_Ext# > 1000),
   
);

CREATE TABLE STUDENT (
    St_ID NUMERIC(6, 0) PRIMARY KEY CHECK (St_ID > 0),
    St_Major CHAR(30),
    St_Cohort NUMERIC(4) NOT NULL,
);

CREATE TABLE COURSE (
    Cr_Code CHAR(8) PRIMARY KEY,
    Cr_Title VARCHAR(40) NOT NULL,
    Cr_CH NUMERIC(2, 0) CHECK (Cr_CH > 0),
    Cr_#ofSec NUMERIC(2, 0) CHECK (Cr_#ofSec > 0),
    Cr_Dept CHAR(4),
    CONSTRAINT FK_COURSE_DEPARTMENT
    FOREIGN KEY (Cr_Dept)
    REFERENCES DEPARTMENT(Dp_Code)
);

CREATE TABLE CBLink (
    Li_CrCode CHAR(8),
    Li_BkID NUMERIC(6, 0),
    Li_usage CHAR(1) CHECK (Li_usage IN ('T', 'R')),
    

    CONSTRAINT FK_CBLink_Course
    FOREIGN KEY (Li_CrCode)
    REFERENCES COURSE(Cr_Code),
    
    CONSTRAINT FK_CBLink_Book
    FOREIGN KEY (Li_BkID)
    REFERENCES BOOK(Bk_ID)
);


CREATE TABLE REGIST (
    Re_BrID NUMERIC(6, 0),
    Re_CrCode CHAR(8),
    Re_Semester CHAR(6) NOT NULL,
  

    CONSTRAINT FK_REGIST_Borrower
    FOREIGN KEY (Re_BrID)
    REFERENCES BORROWER(Br_ID),

    CONSTRAINT FK_REGIST_Course
    FOREIGN KEY (Re_CrCode)
    REFERENCES COURSE(Cr_Code)
);






CREATE TABLE ISSUING (
    is_BrID NUMERIC(6, 0),
    is_BkID NUMERIC(6, 0),
    is_DateTaken DATE NOT NULL,
    is_DateReturn DATE,
	CONSTRAINT is_DateReturn_CH CHECK (is_DateReturn > is_DateTaken),
 
    CONSTRAINT FK_ISSUING_Borrower
    FOREIGN KEY (is_BrID)
    REFERENCES BORROWER(Br_ID),

    CONSTRAINT FK_ISSUING_Book
    FOREIGN KEY (is_BkID)
    REFERENCES BOOK(Bk_ID)
);

INSERT INTO COLLEGE(Cl_Code,Cl_Name ,Cl_Dean)
VALUES('COM' ,'Economy','Prof. Fahim');
INSERT INTO COLLEGE(Cl_Code,Cl_Name ,Cl_Dean)
VALUES('SCI','Science','Prof. Salma');
INSERT INTO COLLEGE(Cl_Code,Cl_Name ,Cl_Dean)
VALUES('EDU ','Education','Dr. Hamad');
select * from COLLEGE;

INSERT INTO DEPARTMENT(Dp_Code ,Dp_Name, Dp_Col, Dp_HoD)
VALUES('INFS ' ,'Information Systems','COM', 'Dr. Kamla');
INSERT INTO DEPARTMENT(Dp_Code ,Dp_Name, Dp_Col, Dp_HoD)
VALUES('FINA  ' ,'Finance ','COM', 'Dr. Salim');
INSERT INTO DEPARTMENT(Dp_Code ,Dp_Name, Dp_Col, Dp_HoD)
VALUES('COMP  ' ,'Computer Science  ','SCI', 'Dr. Zuhoor');
select * from DEPARTMENT ;



