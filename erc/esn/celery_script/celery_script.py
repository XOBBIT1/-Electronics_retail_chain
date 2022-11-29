import random
from esn.models import ObjectModel


def updating_debt():
    try:
        ObjectModel.object.update(debt=random.randint(5, 500),)
    except Exception as e:
        print("Debt didn't changed!")
        raise e
