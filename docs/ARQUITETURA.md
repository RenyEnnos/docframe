# Arquitetura do Infrakit Cru

Este documento explica a organização do framework para quem for manter ou adaptar o Infrakit.

## Objetivo da Arquitetura

Separar o que é fixo do que muda em cada trabalho.

O kit antigo tratava quase tudo como TCC. O Infrakit Cru muda essa lógica: o agente primeiro entende a entrega e só depois adapta rubrica, checklist, contexto, referências e fluxo de trabalho.

## Camadas

### 1. Entrada

`START_AQUI.md` é o ponto inicial. Ele orienta o usuário e o agente.

### 2. Agente

`agente/` contém o comportamento do agente:

- como iniciar;
- quais perguntas fazer;
- quando preencher arquivos;
- como encerrar iterações.

### 3. Core

`core/` contém regras fixas:

- formato final deliberado, com LaTeX como padrão para acadêmico/técnico formal;
- linguagem natural e autoral;
- fontes rastreáveis;
- normas específicas acima de normas genéricas;
- registro das mudanças;
- validação de promessas fortes;
- controle de PDFs e versões;
- checklist LGPD/TI quando aplicável.

Esses arquivos não devem ser alterados em um trabalho comum.

### 4. Modos

`modos/` contém estruturas específicas para tipos de trabalho.

Um modo só deve ser ativado quando o pedido pedir aquela forma de entrega. O primeiro modo criado é proposta institucional/técnica, voltado a documentos de decisão, pilotos, infraestrutura e propostas para instituições.

### 5. Projeto

`projeto/` contém os arquivos vivos. Eles devem ser adaptados pelo agente com base nas respostas do usuário.

Essa camada representa o estado atual do trabalho.

### 6. Logs

`projeto/logs/` guarda detalhes de iterações grandes. O registro principal continua sendo `REGISTRO_ITERACOES.md`.

## Fluxo Esperado

1. Usuário pede para iniciar o Infrakit.
2. Agente lê entrada, core e entrevista.
3. Agente faz perguntas essenciais.
4. Agente roteia modos e módulos necessários.
5. Agente atualiza arquivos vivos.
6. Agente confirma entendimento.
7. Agente adapta rubrica e checklist.
8. Agente começa o trabalho em modo adequado.
9. Agente verifica e registra cada iteração.

## Por Que Não Começar Pelo TCC

Nem todo trabalho precisa de ficha catalográfica, banca, folha de aprovação, resumo em inglês ou estrutura de monografia.

Esses itens devem entrar apenas quando o tipo de trabalho exigir.

## Política de Logs

A arquitetura usa modelo híbrido:

- `REGISTRO_ITERACOES.md` para histórico curto e navegável;
- arquivos em `logs/` para detalhes quando necessário.

Isso evita um arquivo gigante difícil de ler e também evita dezenas de arquivos inúteis para mudanças pequenas.

## Critério de Boa Evolução

Uma nova versão do Infrakit deve:

- reduzir ambiguidade para o agente;
- facilitar uso por usuário leigo;
- manter arquivos organizados;
- evitar duplicação;
- preservar as regras fixas;
- deixar claro o que é específico de cada trabalho.
