progenitor(magali,sally).
progenitor(ninfa,magali).
progenitor(ninfa,sara).
progenitor(ninfa,mario).
progenitor(ninfa,roque).
progenitor(tuto,magali).
progenitor(tuto,sara).
progenitor(tuto,mario).
progenitor(tuto,roque).
progenitor(estela,ninfa).
progenitor(dora,tuto).
progenitor(dora,gachi).

mujer(magali).
mujer(sally).
mujer(ninfa).
mujer(sara).
mujer(estela).
mujer(dora).
mujer(gachi).

hombre(NAME) :- not(mujer(NAME)).

hermano(X,Y) :- (progenitor(Z,X),progenitor(Z,Y));(progenitor(Z,Y),progenitor(Z,X)).

tio(X,Y) :- hermano(X,Z),progenitor(Z,Y).

