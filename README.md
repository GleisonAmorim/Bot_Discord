# Bot de Discord com Integração OpenAI

Este é um bot para Discord que utiliza a API do OpenAI para responder a mensagens com base no histórico do canal. Ele gera respostas utilizando o modelo GPT-3 da OpenAI.

## Requisitos

Antes de executar o bot, é necessário criar um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
DISCORD_BOT_TOKEN=SEU_TOKEN_DO_DISCORD
OPENAI_API_KEY=SUA_CHAVE_DA_API_DO_OPENAI
```

Substitua `SEU_TOKEN_DO_DISCORD` pelo token do seu bot do Discord e `SUA_CHAVE_DA_API_DO_OPENAI` pela chave da API do OpenAI.

## Instalação

1. Clone este repositório:

```
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. Navegue até o diretório do projeto:

```
cd nome-do-repositorio
```

3. Instale as dependências utilizando pip:

```
pip install -r requirements.txt
```

## Execução

Após configurar o arquivo `.env` e instalar as dependências, execute o bot com o seguinte comando:

```
python bot.py
```

## Funcionalidades

- O bot responde a mensagens no canal com base no histórico de mensagens.
- Ele utiliza o modelo GPT-3 da OpenAI para gerar as respostas.
- As respostas são geradas de forma contextual, considerando as mensagens anteriores no canal.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções de bugs. Basta abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
