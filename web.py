#!/usr/bin/python3
import base64
import io

from Overschrijving import Overschrijving
import cgitb
import cgi

cgitb.enable()
form = cgi.FieldStorage()


over = Overschrijving()
datum = form["datum"].value
bedrag = form["bedrag"].value
cent = form["cent"].value
r_opdracht = form["r_opdracht"].value
i_opdracht = form["i_opdracht"].value
r_besch = form["r_besch"].value
b_besch = form["b_besch"].value
i_besch = form["i_besch"].value
mededeling = form["mededeling"].value

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
