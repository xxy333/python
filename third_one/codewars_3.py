
pincode = "-1234"

def validate_pin(pin):
    #return true or false
    if pin.isdigit():
        if len(pin) != 4 and len(pin) !=6:
            return False
        else:
            return True
    else:
        return False





print(validate_pin(pincode))