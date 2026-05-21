# Docframe

Docframe é um kit para orientar agentes de IA na criação, revisão e entrega de documentos com mais controle.

Ele serve para trabalhos acadêmicos, propostas técnicas, currículos, relatórios, documentações e outros textos que precisam de contexto, fontes, critérios de qualidade e registro das decisões.

O Docframe não começa assumindo que seu trabalho é um TCC, artigo ou relatório. Primeiro a IA faz uma entrevista curta, entende o tipo de entrega e adapta os arquivos vivos do projeto. Só depois ela começa a escrever, revisar, pesquisar ou formatar.

## Comece Por Aqui

Você provavelmente não precisa clonar nada manualmente. O jeito mais simples é pedir para a sua IA fazer isso.

Use uma IA que consiga acessar a pasta do seu projeto, ler arquivos e executar comandos quando necessário. Se a sua IA for apenas um chat sem acesso ao seu computador, ela pode explicar o processo, mas não vai conseguir baixar ou modificar os arquivos por você.

Abra sua IA de programação ou escrita e cole este pedido:

```text
Quero usar o Docframe neste trabalho.

Faça o seguinte:

1. Na pasta do meu trabalho, clone ou baixe este repositório:
   https://github.com/RenyEnnos/docframe

2. Deixe o repositório em uma pasta chamada docframe.

3. Depois leia docframe/START_AQUI.md e siga o protocolo.

4. Antes de escrever qualquer entrega final, faça a entrevista inicial comigo.

5. Use minhas respostas para adaptar os arquivos em docframe/projeto/.

6. Ative apenas os modos necessários ao meu tipo de trabalho.

7. Não invente fontes, dados, experiências, normas ou resultados.

8. Registre decisões importantes e pendências durante o trabalho.
```

Se a IA disser que não consegue clonar o repositório, peça para ela baixar o ZIP do GitHub, extrair a pasta e continuar lendo `docframe/START_AQUI.md`.

## Se Você Já Baixou o Docframe

Se a pasta `docframe/` já está dentro da pasta do seu trabalho, diga apenas:

```text
Leia docframe/START_AQUI.md e siga o protocolo do Docframe.
Antes de escrever, faça a entrevista inicial e adapte os arquivos em docframe/projeto/.
```

## O Que a IA Vai Perguntar

A entrevista inicial serve para evitar que a IA comece no caminho errado.

Ela deve perguntar, em linguagem simples:

- que tipo de trabalho você quer fazer;
- qual é o tema;
- quem vai ler ou avaliar;
- qual formato final você precisa;
- se existem regras da instituição, professor, edital ou empresa;
- quais arquivos, PDFs, links ou anotações você já tem;
- se ela pode pesquisar fontes externas;
- qual é o prazo ou nível de urgência.

Você pode responder "não sei". Nesse caso, a IA deve registrar a dúvida como pendência e seguir com uma hipótese conservadora.

## O Que o Docframe Faz

O Docframe ajuda a IA a:

- entender o trabalho antes de escrever;
- separar fatos, hipóteses e pendências;
- montar uma rubrica de qualidade para o tipo de entrega;
- criar checklist de conclusão;
- registrar decisões e iterações;
- controlar fontes e referências candidatas;
- evitar linguagem genérica ou com cara de texto escrito por IA;
- verificar se a entrega está pronta para revisão, submissão ou entrega final.

## O Que o Docframe Não Faz

O Docframe não é um gerador automático de texto.

Ele não deve:

- inventar fontes;
- transformar hipótese em fato;
- prometer resultado sem evidência;
- apagar arquivos do usuário sem pedido explícito;
- instalar ferramentas sem permissão;
- forçar LaTeX quando o formato real de entrega exigir outra stack.

## Arquivos Que a IA Pode Modificar

Durante um trabalho comum, a IA deve modificar principalmente os arquivos em `docframe/projeto/`:

| Arquivo | Para que serve |
|---|---|
| `CONTEXTO_TRABALHO.md` | registra o tipo de trabalho, público, formato, normas e materiais |
| `RUBRICA.md` | define como a qualidade será avaliada |
| `CHECKLIST_ENTREGA.md` | lista o que precisa estar pronto antes da entrega |
| `SCORECARD.md` | registra notas, fragilidades e evolução por iteração |
| `BASE_CONHECIMENTO.md` | guarda fatos confirmados sobre o trabalho |
| `REFERENCIAS_CANDIDATAS.md` | registra fontes possíveis e status de uso |
| `REGISTRO_ITERACOES.md` | mantém o histórico curto das decisões |
| `logs/` | guarda registros maiores quando necessário |

Os arquivos em `core/`, `agente/`, `modos/` e `docs/` são a base do framework. Eles só devem ser alterados quando você estiver melhorando o próprio Docframe, não durante um trabalho normal.

## Regras Permanentes

- LaTeX é o padrão para documentos acadêmicos e técnicos formais.
- Se outro formato for mais adequado ao canal real de entrega, a IA deve registrar a exceção e validar a stack usada.
- Se LaTeX for necessário e não estiver disponível, a IA deve pedir permissão antes de configurar.
- A IA deve preservar a voz do autor.
- O texto não pode ter linguagem genérica, artificial ou com cara de resposta de IA.
- Nenhuma fonte pode ser inventada.
- Normas da instituição, professor, empresa ou edital prevalecem sobre modelos genéricos.
- Toda mudança importante deve ser registrada.
- Fatos, hipóteses e validações devem ser separados.
- Promessas fortes exigem fonte, teste, validação ou reescrita proporcional.

## Para Quem Sabe Usar Terminal

Este passo é opcional. Se você preferir clonar manualmente:

```bash
git clone https://github.com/RenyEnnos/docframe.git docframe
```

Depois disso, abra sua IA e diga:

```text
Leia docframe/START_AQUI.md e siga o protocolo do Docframe.
```

## Filosofia

O objetivo do Docframe é simples: fazer a IA perguntar melhor, organizar melhor, escrever com mais critério e deixar rastreável o que foi decidido.

Menos improviso, menos retrabalho e mais controle sobre a qualidade final.
