select cr_dept , count(*), max(cr_CH)
from course
group by cr_dept
order by 3 ;

select dp_name, sum(bk_totalCopies)
from department,book,course,CBlink
where dp_code= cr_dept
and bk_id =li_bkId
and cr_code= li_crCode
group by dp_name;

/*LAB 4 */
/*6.a*/
SELECT * FROM college;
/*6.b*/
SELECT * FROM borrower WHERE br_type = 'S';
SELECT * FROM book WHERE bk_#ofPages > 100;
/*6.c*/
SELECT * 
FROM employee 
WHERE em_id = (SELECT MAX(em_id) FROM employee);
/*6.d*/
SELECT d.dp_name, c.cl_name
FROM department d
JOIN college c ON d.dp_col = c.cl_code;

/*6.e*/
SELECT cl_name, COUNT(*) AS record_count
FROM college
GROUP BY cl_name;

/*6.f*/
SELECT Cl_Code+' ' + cl_name AS calculated_column
FROM college;



/*EX15/6*/
/*Q1*/
select bk_title, cr_title
from book,course,CBlink
where li_bkId = bk_id and li_crCode = cr_code;

/*Q2*/
select bk_title
from book
WHERE bk_totalCopies > 50 AND bk_totalCopies <= 100;

/*Q3*/
select DISTINCT br_dept 
from borrower ,department
where br_city = 'Seeb'
ORDER BY br_dept DESC;



/*LAB 5*/
/*1.a*/
ALTER TABLE regist 
 ADD re_serial# INT;

/*1.b*/
CREATE SEQUENCE seq_regist_serial# 
START WITH 1
INCREMENT BY 2;


/*1.c*/
UPDATE regist
SET re_serial# = NEXT VALUE FOR seq_regist_serial#;

/*1.d*/
INSERT INTO regist (re_brID, re_crCode, re_semester, re_serial#)
VALUES (92120, 'COMP4201', 'FL2015',NEXT VALUE FOR seq_regist_serial# ),
       (10021, 'COMP4202', 'FL2016',NEXT VALUE FOR seq_regist_serial# );

/*2.a*/
ALTER TABLE CBlink 
 ADD li_key char(8);

/*2.b*/
CREATE SEQUENCE seq_CBlink_key
START WITH 0
INCREMENT BY 1
MINVALUE  0
MAXVALUE 9999
CYCLE;

/*2.c*/
 UPDATE CBlink
SET li_key = LEFT(li_crCode, 4) + RIGHT('0000' + CAST(NEXT VALUE FOR seq_CBlink_key AS VARCHAR(4)), 4);

/*2.3*/
 
INSERT INTO CBlink (li_crCode, li_bkId, li_usage,li_key)
VALUES ('COMP4201 ', '2001', 'T','COMP'+ RIGHT('0000' + CAST(NEXT VALUE FOR seq_CBlink_key AS VARCHAR(4)), 4));
      
select * from CBlink
/*2.4*/
CREATE UNIQUE INDEX In_book ON book(bk_title);
	