#!/usr/bin/python3
import base64
import io

from Overschrijving import Overschrijving
import cgitb
import cgi

cgitb.enable()
form = cgi.FieldStorage()


over = Overschrijving()
over.set_waarde(datum=form["datum"], bedrag=form["bedrag"], cent=form["cent"], r_opdracht=form["r_opdracht"],
                i_opdracht=form["i_opdracht"], r_besch=form["r_besch"], b_besch=form["b_besch"],
                i_besch=form["i_besch"], mededeling=form["mededeling"])
over.schrijf()
imgByteArr = io.BytesIO()
over.get_image().save(imgByteArr, format='PNG')
imgByteArr = imgByteArr.getvalue()
data_uri = base64.b64encode(imgByteArr).decode('utf-8').replace('\n', '')
img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)

print("Content-Type: text/html;charset=utf-8")
print(img_tag)
