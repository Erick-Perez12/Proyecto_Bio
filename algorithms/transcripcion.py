def transcripcion_adn_arn(secuencia_adn):
    secuencia_adn = secuencia_adn.upper()
    transcripcion = {
        'A': 'U',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    secuencia_arn = ""
    for base in secuencia_adn:
        if base in transcripcion:
            secuencia_arn += transcripcion[base]
        else:
            secuencia_arn += "N"  
    
    return secuencia_arn
