# DECORADORES

from loguru import logger

logger.add("Meu_app.log") # Cria um arquivo de log

def soma(x: int,y: int) -> int:
    logger.info(x)
    logger.info(y)
    logger.info(x+y)
    return x+y

print(soma(2,3))

# Foi falando um pouco sobre sentry e datadog, e suas diferençcas para o loguru (Retomar de 35:15)