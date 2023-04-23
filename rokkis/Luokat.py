from flask import Flask, Response, request
import json
from flask_cors import CORS
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='funland',
    user='root',
    password='j44j44j44',
    autocommit=True
)

class Player:
    def __init__(self, name, location, fuel, score):
        self.name = name
        self.location = location
        self.fuel = fuel
        self.score = score
        self.käydytmaat = []

    def newPlayer(self, name, location):
        sql = "INSERT INTO game(name, fuel, score, location) VALUES ('{}','{}','{}')".format(name, 1000, 0, location)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        yhteys.commit()

    def id_search(self, name):
        sql = "SELECT id FROM game WHERE name ='" + name + "'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        for i in kursori:
            for a in i:
                return a


class Airport:

    def visitedCountries(self, location):
        sql = "INSERT INTO tracker(game_id, country_name) VALUES ('{}','{}')".fromat(self.name, location)

    def haku(self, id):
        sql = "SELECT iso_country from country";
        kursori = yhteys.cursor()
        kursori.execute(sql)
        alista = []
        for i in kursori:
            alista.append(i)
        sql = "SELECT country_name FROM tracker WHERE game_id = (SELECT id FROM game WHERE name ='" + str(id) + "')"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        olista = []
        for i in kursori:
            olista.append(i)
        lista = []
        for i in alista:
            if i not in olista:
                for a in i:
                    lista.append(a)
        return lista


class Question:
   def __init__(self, name)


