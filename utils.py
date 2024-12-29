def ano_invalido(ano):

    if not ano:
        return "Ano é obrigatório"
    
    try:
        ano_int = int(ano)
    except ValueError as e:
        return "Ano inválido. Informe apenas numeros entre 1970 e 2023"
    
    if ano_int > 2023 or ano_int < 1970:
        return "Ano inválido. Informe apenas numeros entre 1970 e 2023"
    
    return None