def is_empty_form(form_data):
    # Recorre el array de campos para ver si el form es vacio o no
    if len(form_data.keys()) == 1:
        return True
    for key in list(form_data.keys())[1:]:
        if not form_data[key]:
            return True
    return False

def fill_form_values(fields, form):
    ''' 
      Le recargo al formulario los valores que puso el cliente
    '''
    for field in fields['fields']:
        field['value'] = form.get(field['name'])
    return fields