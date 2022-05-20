# -*- coding: utf-8 -*-
"""
Created on Thu May 19 17:12:00 2022

@author: Asus
"""

from pyswip import Prolog
prolog = Prolog()

prolog.assertz("abuelo(vicente,amed)")
prolog.assertz("abuelo(vicente,fatima)")
prolog.assertz("hijo(marcos,vicente)")
prolog.assertz("hija(paty,vicente)")
prolog.assertz("primo(amed,fatima)")
prolog.assertz("padre(marcos,amed)")
prolog.assertz("hermano(marcos,paty)")
prolog.assertz("hermana(paty,marcos)")
prolog.assertz("nieto(amed,vicente)")
prolog.assertz("hijo(amed,marcos)")


#list(prolog.query("padre(juan,X)"))==[{"X":"maria"},{"Y":"julio"}]

for elemento in prolog.query("abuelo(X,Y)"):
    print(elemento["X"], "es el abuelo de",elemento["Y"])
for elemento in prolog.query("primo(Y,Z)"):
    print(elemento["Y"], "es el primo de",elemento["Z"])
for elemento in prolog.query("padre(X,Y)"):
    print(elemento["X"], "es el padre de",elemento["Y"])


for elemento in prolog.query("hijo(X,Y)"):
    print(elemento["X"], "es el hijo de",elemento["Y"])
for elemento in prolog.query("hija(X,Y)"):
    print(elemento["X"], "es la hija de",elemento["Y"])
for elemento in prolog.query("hermano(X,Y)"):
    print(elemento["X"], "es el hermano de",elemento["Y"])

for elemento in prolog.query("hermana(X,Y)"):
    print(elemento["X"], "es la hermana de",elemento["Y"])

for elemento in prolog.query("nieto(X,Y)"):
    print(elemento["X"], "es el nieto de",elemento["Y"])