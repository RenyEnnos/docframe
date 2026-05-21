# Infrakit Cru

Infraestrutura base para orientar agentes de IA na criação, revisão e entrega de trabalhos acadêmicos, técnicos e profissionais com formato final deliberado.

O Infrakit Cru não começa assumindo que o trabalho é um TCC, artigo, relatório ou seminário. Primeiro o agente entrevista o usuário, entende o tipo de entrega e adapta os arquivos vivos do projeto. Só depois ele passa a escrever, revisar, pesquisar ou formatar.

## Para Quem é

Este kit é para estudantes e autores que querem trabalhar com um agente de IA de forma organizada, sem perder contexto, sem texto genérico e sem transformar o projeto em uma pasta bagunçada.

O leitor esperado é um usuário leigo. Depois de ler este arquivo, ele deve conseguir iniciar uma sessão com o agente e entender quais arquivos podem ser modificados.

## Como Usar

1. Coloque a pasta `infrakit_cru/` dentro da pasta do seu trabalho.
2. Inicie o agente e diga:

```text
Leia infrakit_cru/START_AQUI.md e siga o protocolo.
```

3. Responda à entrevista inicial.
4. Informe se o agente deve usar apenas materiais fornecidos por você ou se pode pesquisar.
5. O agente vai adaptar os arquivos em `projeto/`.
6. Depois da adaptação, o agente trabalha por iterações registradas.

## Estrutura

| Área | Função |
|---|---|
| `START_AQUI.md` | Entrada simples para usuário e agente |
| `agente/` | Protocolo de comportamento e entrevista inicial |
| `core/` | Regras fixas que não dependem do tipo de trabalho |
| `modos/` | Modelos específicos ativados conforme o tipo de entrega |
| `projeto/` | Arquivos vivos que o agente adapta após entrevistar o usuário |
| `projeto/logs/` | Registros detalhados de iterações maiores |
| `docs/` | Explicação da arquitetura e decisões do framework |

## Regras Permanentes

- LaTeX é o padrão para documentos acadêmicos e técnicos formais.
- Se outro formato for mais adequado ao canal real de entrega, o agente deve registrar a exceção e validar a stack usada.
- Se LaTeX for necessário e não estiver disponível, o agente deve pedir permissão antes de configurar.
- O agente deve preservar a voz do autor.
- O texto não pode ter linguagem genérica, artificial ou com cara de resposta de IA.
- Nenhuma fonte pode ser inventada.
- Normas da instituição, professor ou edital prevalecem sobre modelos genéricos.
- Toda mudança importante deve ser registrada.
- Fatos, hipóteses e validações devem ser separados.
- Promessas fortes exigem fonte, teste, validação ou reescrita proporcional.

## Filosofia

O Infrakit não é um gerador automático de texto. Ele é uma estrutura de trabalho. A função dele é fazer o agente perguntar melhor, organizar melhor, escrever com mais critério e deixar rastreável o que foi decidido.

O objetivo é simples: menos improviso, menos retrabalho e mais controle sobre a qualidade final.
