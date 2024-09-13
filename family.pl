
father_of(joe, paul).
father_of(joe, mary).
mother_of(jane, paul).
mother_of(jane, mary).
male(paul).
male(joe).

female(mary).
female(jane).



male(X) :- father_of(X, _).
female(X) :- mother_of(X, _).

son_of(X, Y) :- father_of(Y, X), male(X).
son_of(X, Y) :- mother_of(Y, X), male(X).


daughter_of(X, Y) :- father_of(Y, X), female(X).
daughter_of(X, Y) :- mother_of(Y, X), female(X).

sibling_of(X, Y) :- father_of(Z, X), father_of(Z, Y), X \= Y.
sibling_of(X, Y) :- mother_of(Z, X), mother_of(Z, Y), X \= Y.





