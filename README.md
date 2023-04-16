# Registro de treino

Realizar o registro do treino em uma tabela no Google Sheet. Registrando data, hora, atividade realizada e sua duração.

Informando a atividade e as características corporais, a API NUTRITIONIX realiza o calculo das calorias gastas de acordo com os dados informados.
O equivalente metabólico (MET) é uma medida que estima o gasto energético com atividade física.

Essa informações é interpretada pelo NUTRITIONIX, o retorno da API gravamos em nossa tabela com a API SHEETY.

NUTRITIONIX - Essa API processa a linguagem natual(NLP) e retorna não só ativiades físicas mas também tabelas nutricional.

URL: https://developer.nutritionix.com/

demo: https://www.nutritionix.com/natural-demo/exercise

SHEETY- Vinculando com a sua conta Google é possivel gravar informações diretamente nas planilhas selecionada.

URL: https://sheety.co/

# Instalação

Basta instalar a biblioteca "requests" para ter acesso as APIs. Já as bibliotes "os" e "datatime" já vem com Python.

```bash
pip install requests
```

# Execução

É necessário a criação de uma conta no site das API para que seja gerada as chaves e as IDs altenticação de uso das APIs.
Informe as chaves e as IDs nas variáveis de ambiente do Python para acesso as contas criadas. Leia na documentação da API, como configurar seus dados.

NUTRITIONIX = https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.gz6pu9o7f9iz

SHEETY = https://sheety.co/docs/authentication.html

** IMPORTANTE **

O ENDPOINT da API SHEETY é gerado dinamicamente para cada projeto, sendo assim é necessário armazenado também nas variáveis de ambiente.

Execute o arquivo main.py em seu interpretador Python, em seguida será solicitado no prompt a atividade executada.
OBS.: Altere os dados pessoais no dicionário "exercise_data" para que o calculo sejá de acordo com suas características.

Em seguida os dados serão gravados na planilha informada na API SHEETY.

# Licença

[MIT](https://choosealicense.com/licenses/mit/)
