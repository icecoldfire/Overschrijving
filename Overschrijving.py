from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Overschrijving:
    spatie_x = 4
    box_x = 26

    spatie_y = 2
    box_y = 22

    offset_y = 7
    offset_y_klein = 2
    len_regel = 26

    loc_datum_x = 23
    loc_datum_y = 142 - offset_y

    loc_bedrag_x = 892
    loc_bedrag_y = loc_datum_y
    len_bedrag = 8

    loc_cent_x = 1162
    loc_cent_y = loc_datum_y
    len_cent = 2

    loc_r_opdracht_x = 203
    loc_r_opdracht_y = 192 - offset_y

    loc_i_opdracht_x = loc_r_opdracht_x
    loc_i_opdracht_y = 248 - offset_y_klein

    loc_r_besch_x = loc_r_opdracht_x
    loc_r_besch_y = 342 - offset_y

    loc_b_besch_x = loc_r_opdracht_x
    loc_b_besch_y = 392 - offset_y

    loc_i_besch_x = loc_r_opdracht_x
    loc_i_besch_y = 448 - offset_y_klein

    loc_mededeling_x = loc_r_opdracht_x
    loc_mededeling_y = 543 - offset_y

    def __init__(self, **kwargs):
        # font = ImageFont.truetype(<font-file>, <font-size>)
        self.font = ImageFont.truetype("cour.ttf", 45)
        self.font_klein = ImageFont.truetype("cour.ttf", 24)
        self.reset()
        self.set_waarde(**kwargs)

    def reset(self):
        self.img = Image.open("Overschrijvingsformulier.png").convert('RGBA')
        self.draw = ImageDraw.Draw(self.img, 'RGBA')

    def set_waarde(self, datum="", bedrag="", cent="00", r_opdracht="", i_opdracht="",
                   r_besch="", b_besch="", i_besch="", mededeling=""):
        self.datum = str(datum)
        self.bedrag = str(bedrag)
        self.cent = str(cent)
        self.r_opdracht = str(r_opdracht)
        self.i_opdracht = str(i_opdracht)
        self.r_besch = str(r_besch)
        self.b_besch = str(b_besch)
        self.i_besch = str(i_besch)
        self.mededeling = str(mededeling)

    @staticmethod
    def offset_x(lengte, aantal):
        return (lengte - aantal) * (Overschrijving.box_x + Overschrijving.spatie_x)

    def schrijf(self):
        self.schrijf_string(Overschrijving.loc_datum_x, Overschrijving.loc_datum_y, self.datum)

        self.schrijf_string(Overschrijving.loc_bedrag_x, Overschrijving.loc_bedrag_y, self.bedrag,
                            lengte=Overschrijving.len_bedrag)

        self.schrijf_string(Overschrijving.loc_cent_x, Overschrijving.loc_cent_y, self.cent,
                            lengte=Overschrijving.len_cent)

        self.schrijf_string(Overschrijving.loc_r_opdracht_x, Overschrijving.loc_r_opdracht_y, self.r_opdracht)

        self.schrijf_string(Overschrijving.loc_i_opdracht_x, Overschrijving.loc_i_opdracht_y, self.i_opdracht,
                            font=self.font_klein, max_len=Overschrijving.len_regel)

        self.schrijf_string(Overschrijving.loc_r_besch_x, Overschrijving.loc_r_besch_y, self.r_besch)

        self.schrijf_string(Overschrijving.loc_b_besch_x, Overschrijving.loc_b_besch_y, self.b_besch)

        self.schrijf_string(Overschrijving.loc_i_besch_x, Overschrijving.loc_i_besch_y, self.i_besch,
                            font=self.font_klein, max_len=Overschrijving.len_regel)

        self.schrijf_string(Overschrijving.loc_mededeling_x, Overschrijving.loc_mededeling_y, self.mededeling)

    def schrijf_string(self, x, y, string, lengte=None, font=None, max_len=-1):
        if not lengte:
            lengte = len(string)
        off_x = x + Overschrijving.offset_x(lengte, len(string))
        off_y = y
        char = 0
        for i in string:
            if char == max_len or i == '\n':
                off_y += Overschrijving.spatie_y + Overschrijving.box_y
                off_x = x + Overschrijving.offset_x(lengte, len(string))
                char = 0
                if i.isspace():
                    continue
            self.schrijf_leter(off_x, off_y, i, font=font)
            off_x += Overschrijving.offset_x(1, 0)
            char += 1

    def schrijf_leter(self, x, y, letter, font=None):
        if not font:
            font = self.font
        # draw.text((x, y),"Sample Text",(r,g,b))
        self.draw.text((x, y), letter, (0, 0, 0, 0), font=font)

    def save(self, uit='out.png'):
        self.img.save(uit, "PNG")

    def run(self):
        self.schrijf()
        self.save()


if __name__ == "__main__":
    overschrijving = Overschrijving(datum="041216", bedrag="1234", cent="12", r_opdracht="BE13736001704739",
                                    i_opdracht="Stijn Goethals\nSchriek 321 2180 Ekeren België",
                                    r_besch="BE13736001704739", b_besch="KREDBEBB ",
                                    i_besch="Stijn Goethals Schriek 321 2180 Ekeren", mededeling="Donatie")
    overschrijving.run()
