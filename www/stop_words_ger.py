﻿#!/usr/bin/python3
# -*- coding: utf-8 -*-

#==============================================================================
# stop_words_ger.py
#
# This file includes german stop words to exclude form word cloud calculations
#==============================================================================

dict = {
"–" : 0,
"\–" : 0,
"\\–" : 0,
"--": 0,
"->" : 0,
"2" : 0,
"3" : 0,
"'n": 0,
"a": 0,
"aber" : 0,
"alle" : 0,
"allem" : 0,
"allen" : 0,
"aller" : 0,
"alles" : 0,
"als" : 0,
"also" : 0,
"am" : 0,
"an" : 0,
"andere" : 0,
"anderem" : 0,
"anderen" : 0,
"anderer" : 0,
"anderes" : 0,
"anders" : 0,
"auch" : 0,
"auf" : 0,
"aus" : 0,
"bei" : 0,
"beim" : 0,
"bin" : 0,
"bis" : 0,
"bist" : 0,
"da" : 0,
"damit": 0,
"dann" : 0,
"dadurch" : 0,
"daher" : 0,
"darum" : 0,
"das" : 0,
"daß" : 0,
"dass" : 0,
"dazu" : 0,
"dein" : 0,
"deine" : 0,
"deinem" : 0
"deinen" : 0
"deiner" : 0
"deines" : 0
"dem" : 0,
"den" : 0,
"denen": 0,
"denn" : 0,
"der" : 0,
"derer" : 0,
"dasselbe" : 0,
"derselbe" : 0,
"derselben" : 0,
"denselben" : 0,
"desselben" : 0,
"dieselbe" : 0,
"dieselben" : 0,
"des" : 0,
"dessen" : 0,
"deshalb" : 0,
"dh" : 0,
"dich" : 0,
"die" : 0,
"dies" : 0,
"diese" : 0,
"diesem" : 0,
"diesen" : 0,
"dieser" : 0,
"dieses" : 0,
"dir" : 0,
"doch" : 0,
"dort" : 0,
"du" : 0,
"durch" : 0,
"e" : 0,
"eben" : 0,
"eigentlich": 0, 
"ein" : 0,
"eine" : 0,
"einem" : 0,
"einen" : 0,
"einer" : 0,
"eines" : 0,
"einig" : 0,
"einige" : 0,
"einigem" : 0,
"einigen" : 0,
"einiger" : 0,
"einiges" : 0,
"einmal" : 0,
"er" : 0,
"es" : 0,
"euch" : 0,
"euer" : 0,
"eure" : 0,
"f" : 0,
"für" : 0,
"gab": 0,
"gar" : 0,
"geht" : 0,
"gemacht" : 0,
"gesagt" : 0,
"gibt" : 0,
"gibts": 0,
"gibt's": 0,
"glaube": 0,
"glauben": 0,
"hab" : 0,
"habe" : 0,
"haben" : 0,
"habt" : 0,
"halt": 0,
"hast": 0,
"hat" : 0,
"hatte" : 0,
"hatten" : 0,
"hattest" : 0,
"hattet" : 0,
"herald" : 0,
"hier" : 0,
"hin" : 0,
"hinter" : 0,
"ich" : 0,
"ihn" : 0,
"ihm" : 0,
"ihr" : 0,
"ihre" : 0,
"ihrem" : 0,
"ihren" : 0,
"ihrer" : 0,
"ihres" : 0,
"im" : 0,
"immer" : 0,
"in" : 0,
"ist" : 0,
"ja" : 0,
"jede" : 0,
"jedem" : 0,
"jeden" : 0,
"jeder" : 0,
"jedes" : 0,
"jenen" : 0,
"jener" : 0,
"jenes" : 0,
"jetzt" : 0,
"k" : 0,
"kann" : 0,
"kannst" : 0,
"kein" : 0,
"keine" : 0,
"keinem" : 0,
"keinen" : 0,
"keiner" : 0,
"keines" : 0,
"können" : 0,
"könnt" : 0,
"könnte" : 0,
"kommen" : 0,
"kommt" : 0,
"machen" : 0,
"macht" : 0,
"manche" : 0,
"manchem" : 0,
"manchen" : 0,
"mancher" : 0,
"manches" : 0,
"mal" : 0,
"man" : 0,
"mein" : 0,
"meine" : 0,
"meinem" : 0,
"meinen" : 0,
"meiner" : 0,
"meines" : 0,
"mich" : 0,
"mir" : 0,
"mit" : 0,
"möchte": 0,
"muß" : 0,
"muss" : 0,
"mußt" : 0,
"musst" : 0,
"musste" : 0,
"müssen" : 0,
"müßt" : 0,
"nach" : 0,
"nachdem" : 0,
"ne" : 0,
"nein" : 0,
"'nen": 0,
"nicht" : 0,
"nichts" : 0,
"noch" : 0,
"nun" : 0,
"nur" : 0,
"ob" : 0,
"oder" : 0,
"ohne" : 0,
"sage" : 0,
"sagen" : 0,
"sagt" : 0,
"sagte" : 0,
"schon" : 0,
"sehen" : 0,
"sehr" : 0,
"seid" : 0,
"sein" : 0,
"seine" : 0,
"seinem" : 0,
"seinen" : 0,
"seiner" : 0,
"seines" : 0,
"selbst" : 0,
"sich" : 0,
"sie" : 0,
"sind" : 0,
"s" : 0,
"so" : 0,
"solche" : 0,
"solchem" : 0,
"solchen" : 0,
"solcher" : 0,
"solches" : 0,
"soll" : 0,
"sollen" : 0,
"sollst" : 0,
"sollt" : 0,
"sollte" : 0,
"sondern" : 0,
"sonst" : 0,
"soweit" : 0,
"sowie" : 0,
"über" : 0,
"um" : 0,
"und" : 0,
"unser" : 0,
"unsere" : 0,
"unserer": 0,
"uns" : 0,
"unse" : 0,
"unsem" : 0,
"unsen" : 0,
"unser" : 0,
"unses" : 0,
"unter" : 0,
"viel" : 0,
"vom" : 0,
"von" : 0,
"vor" : 0,
"während" : 0,
"wann" : 0,
"war" : 0,
"waren" : 0,
"warst" : 0,
"warum" : 0,
"was" : 0,
"weg" : 0,
"weil" : 0,
"weiter" : 0,
"weitere" : 0,
"welche" : 0,
"welchem" : 0,
"welchen" : 0,
"welcher" : 0,
"welches" : 0,
"wenn" : 0,
"wer" : 0,
"werde" : 0,
"werden" : 0,
"werdet" : 0,
"weshalb" : 0,
"wie" : 0,
"wieder" : 0,
"wieso" : 0,
"will" : 0,
"wir" : 0,
"wird" : 0,
"wirklich" : 0,
"wirst" : 0,
"wo" : 0,
"woher" : 0,
"wohin" : 0,
"wollen" : 0,
"wollte" : 0,
"wurde" : 0,
"würde": 0,
"wurden" : 0,
"würden" : 0,
"zb" : 0,
"zu" : 0,
"zum" : 0,
"zur" : 0,
"zwar" : 0,
"zwischen" : 0,
}