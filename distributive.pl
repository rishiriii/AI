male(raj).
male(aayush).
doctor(raj).
engineer(aayush).
sa(X):-male(X),(doctor(X);engineer(X)).
as(X):-((male(X),doctor(X));(male(X),engineer(X))).
