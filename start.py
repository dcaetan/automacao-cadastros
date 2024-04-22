import pyautogui as pyatg
import time

pyatg.PAUSE = 0.8

# Passo 1: Entrar no site desejado
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

    # 1.1 Abrir o navegador
pyatg.press("win")
pyatg.write("Microsoft Edge")
pyatg.press("enter")

    # 1.2 Acessar a pagina web
time.sleep(0.5)
url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyatg.write(url)
pyatg.press("enter")

# Passo 2: Fazer login com credenciais validas
    # 2.1 Escreve o e-mail e passa para o proximo campo (senha)
time.sleep(0.5)
pyatg.click(x=659, y=356) # Seleciona uma area da tela para clicar com o mouse
pyatg.write("adm@python.com")
pyatg.press("tab")
    # 2.2 - Escreve a senha e "loga/entra"
pyatg.write("password")
pyatg.press("tab")
pyatg.press("space")