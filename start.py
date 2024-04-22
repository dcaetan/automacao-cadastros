import pyautogui as pa
import pandas as pd
import time

pa.PAUSE = 0.8

# Passo 1: Entrar no site desejado
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

    # 1.1 Abrir o navegador
pa.press("win")
pa.write("Microsoft Edge")
pa.press("enter")

    # 1.2 Acessar a pagina web
time.sleep(0.5)
url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pa.write(url)
pa.press("enter")

# Passo 2: Fazer login com credenciais validas
    # 2.1 Escreve o e-mail e passa para o proximo campo (senha)
time.sleep(0.5)
pa.click(x=659, y=356) # Seleciona uma area da tela para clicar com o mouse
pa.write("adm@python.com")
pa.press("tab")
    # 2.2 - Escreve a senha e "loga/entra"
pa.write("password")
pa.press("tab")
pa.press("space")

# Passo 3: Importar base de dados (.csv)
tabela = pd.read_csv("data_base/produtos.csv")
#print(tabela)

# Passo 4: Cadastrar os produtos
time.sleep(0.5)
for linha in tabela.index: # .index = linha da tabela | .columns = culuna da tabela
    pa.click(x=682, y=244)

    codigo = tabela.loc[linha, "codigo"]
    pa.write(codigo)
    pa.press("tab")

    marca = tabela.loc[linha, "marca"]
    pa.write(marca)
    pa.press("tab")

    pa.write(tabela.loc[linha, "tipo"])
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "categoria"]))
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "preco_unitario"]))
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "custo"]))
    pa.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs): # .isna = Verifica se o campo está vazio
        pa.write(obs)
    pa.press("tab")
    pa.press("space")
    #pa.scroll(1000)
    pa.press("home")  