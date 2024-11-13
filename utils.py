from typing import Union
from traceback import print_exc
def str2number(text: str,
               print_exception: bool = True) -> Union[None, int, float]:
    """ Función que transforma un texto en un entero.

    Args:
        texto (str): Texto con formato de entero.
        print_exception (bool): Si esta en True muestra el mensaje de la excepción.

    Returns:
        Union[None, int, float]: Retorna un entero o None en caso de error.
    """
    try:
        return int(text.strip())
    except Exception as ex:
        try:
            return float(text.strip())
        except Exception as ex:
            if print_exception:
                print_exc()
    return None


def input_number(message: str,
                 error_message: str,
                 integer: bool = False,
                 repeat: bool = True) -> Union[None, int, float]:
    """ Se utiliza para ingresar un número.

    Args:
        message (str): Texto que muestra el input.
        error_message (str): Texto que se muestra en caso de error.
        integer (bool): Se está en True retorna un entero, en caso contrario
            retorna un flotante. Defaults to False.
        repeat (bool): Si está en True obliga a que se ingrese un número.
        
    Returns:
        Union[None, int, float]: Retorna un None, int o float.
    """
    while True:
        input_data = input(message)
        data = str2number(text=input_data, print_exception=False)
        if data is not None:
            return int(data) if integer else float(data)
        else:
            if error_message is not None and len(error_message) > 0:
                print(error_message)
        if not repeat:
            return None