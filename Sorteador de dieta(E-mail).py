import random
import win32com.client as win32

folhosos = ["Couve refogada - 2 colheres de sopa", "Alface - 4 folhas"]
legumes = ["Cenoura cozida - 75g", "Brócolis cozido - 120g", "Tomate salada - 90g"]
carnes = ["Filé de frango grelhado - 100g", "Patinho sem gordura grelhado - 80g", "Peixe grelhado - 120g", "Filé mignion assado - 100g"]
carboidratos = ["Macarrão - 120g", "Arroz branco - 100g", "Purê de batata ou aipim - 250g", "Batata cozida - 300g"]
feijoes = ["Feijão preto - 65g", "Feijão fradinho - 65g"]


def almocos():
    sorteio = f"""
        <p>{random.choice(folhosos)}</p>
        <p>{random.choice(legumes)}</p>
        <p>{random.choice(carnes)}</p>
        <p>{random.choice(carboidratos)}</p>
        <p>{random.choice(feijoes)}</p>"""

    return sorteio


almoco_seg = almocos()
almoco_ter = almocos()
almoco_qua = almocos()
almoco_qui = almocos()
almoco_sex = almocos()

outlook = win32.Dispatch("outlook.application")
email = outlook.CreateItem(0)

email.To = "@gmail.com"
email.subject = "Cardápio da semana"
email.HTMLBody = f"""
<p>Olà!</p>
<p>Estes são os almoços da semana:</p>

<hr>

<p>SEGUNDA:</p>
<p>{almoco_seg}</p>

<hr>

<p>TERÇA:</p>
<p>{almoco_ter}</p>

<hr>

<p>QUARTA:</p>
<p>{almoco_qua}</p>

<hr>

<p>QUINTA:</p>
<p>{almoco_qui}</p>

<hr>

<p>SEXTA:</p>
<p>{almoco_sex}</p>

<hr>

<p>Espero que goste!</p>
"""

email.Send()
print("Email enviado com sucesso!")
