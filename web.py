# -*- coding: utf-8 -*-
#!/usr/bin/python3
import base64
import io

from Overschrijving import Overschrijving
import cgitb
import cgi

cgitb.enable()
form = cgi.FieldStorage()


over = Overschrijving()
try:
    datum = form["datum"].value
except KeyError:
    datum = ""
try:
    bedrag = form["bedrag"].value
except KeyError:
    bedrag = ""
try:
    cent = form["cent"].value
except KeyError:
    cent = ""
try:
    r_opdracht = form["r_opdracht"].value
except KeyError:
    r_opdracht = ""
try:
    i_opdracht = form["i_opdracht"].value
except KeyError:
    i_opdracht = ""
try:
    r_besch = form["r_besch"].value
except KeyError:
    r_besch = ""
try:
    b_besch = form["b_besch"].value
except KeyError:
    b_besch = ""
try:
    i_besch = form["i_besch"].value
except KeyError:
    i_besch = ""
try:
    mededeling = form["mededeling"].value
except KeyError:
    mededeling = ""

over.set_waarde(datum=datum, bedrag=bedrag, cent=cent, r_opdracht=r_opdracht, i_opdracht=i_opdracht, r_besch=r_besch,
                b_besch=b_besch, i_besch=i_besch, mededeling=mededeling)
over.schrijf()
imgByteArr = io.BytesIO()
over.get_image().save(imgByteArr, format='PNG')
imgByteArr = imgByteArr.getvalue()
data_uri = base64.b64encode(imgByteArr).decode('utf-8').replace('\n', '')
img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
print("Content-Type: text/html;charset=utf-8\n\n\n\n")
print(img_tag)
