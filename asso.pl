student(raj).
student(rahul).
hscstudent(raj).
sscstudent(raj).
sscstudent(rahul).
lbscitadmission(X):-((student(X),hscstudent(X)),sscstudent(X)).
rbscitadmission(X):-(student(X),(hscstudent(X),sscstudent(X))).
