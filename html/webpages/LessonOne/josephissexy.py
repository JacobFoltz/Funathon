def sub(*args,**kwargs):
        try:
            result_place = Element("output2")
            multiplier = int(Element("num").value)
            if multiplier < 0:
                raise ValueError
        except ValueError:
            result_place.write("Please enter a real, positive integer")
        else:
            result_place.write("${:.2f}".format(1.1*multiplier))