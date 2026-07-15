# Docframe

Docframe é um protocolo documental leve para orientar agentes de IA na criação, revisão, pesquisa, formatação e entrega de documentos com estado explícito, fontes rastreáveis e critérios verificáveis.

Ele pode ser usado em trabalhos acadêmicos, currículos, propostas, relatórios, documentação técnica, apresentações, planilhas, formulários, e-mails e outros artefatos. O formato final é uma decisão do projeto; PDF e LaTeX são opções, não destinos obrigatórios.

## O que o Docframe não é

- não é um gerador genérico de textos;
- não é uma aplicação SaaS ou um framework agentivo pesado;
- não depende de um modelo, IDE, fornecedor ou formato específico;
- não transforma hipótese em fato nem fonte encontrada em fonte validada;
- não autoriza instalação, exclusão, envio, publicação ou outra ação irreversível sem permissão explícita.

## Começar

Na pasta que contém `docframe/`, diga ao agente:

```text
Leia o protocolo do Docframe, identifique o estado atual e conduza o próximo passo necessário.
```

O ponto de entrada é `START_AQUI.md`. O agente deve ler somente o núcleo mínimo, verificar `projeto/CONTEXTO_TRABALHO.md` e carregar módulos adicionais conforme o estado e o tipo de entrega.

## Primeiro uso

1. O agente extrai do pedido tudo o que já foi informado.
2. Registra lacunas que realmente podem mudar o trabalho.
3. Faz perguntas progressivas; o usuário pode responder “não sei”.
4. Só libera produção quando o gate de contexto mínimo possui evidência.
5. Planeja, produz, verifica e declara exatamente para que a entrega está pronta.

### Exemplo curto

```text
Usuário: preciso revisar este currículo e entregar em DOCX.
Agente: registra produto, público, formato e materiais; ativa o modo de currículo;
        pergunta apenas pela oportunidade-alvo e por fatos ainda não confirmados;
        produz o DOCX; inspeciona o arquivo real; registra evidências e prontidão.
```

## Arquivos vivos

Durante um trabalho normal, o agente atualiza principalmente `projeto/`:

| Arquivo | Fonte de verdade para |
|---|---|
| `CONTEXTO_TRABALHO.md` | estado atual, objetivo, produto, contexto mínimo, bloqueadores e próxima ação |
| `DECISOES.md` | decisões vigentes e suas substituições |
| `REFERENCIAS_CANDIDATAS.md` | fontes, inspeção, confiabilidade e incorporação |
| `AFIRMACOES.md` | afirmações materiais e ligação com evidências |
| `RUBRICA.md` | critérios atômicos da entrega |
| `SCORECARD.md` | avaliações executadas e evidências observadas |
| `CHECKLIST_ENTREGA.md` | gates objetivos e bloqueadores |
| `BASE_CONHECIMENTO.md` | resumo derivado dos registros canônicos |
| `REGISTRO_ITERACOES.md` | histórico curto, transições e motivo de parada |

Os contratos e a precedência entre arquivos estão em `docs/CONTRATOS_ARQUIVOS.md`.

## Como o usuário mantém controle

- mudanças de objetivo, formato, autoridade ou escopo reabrem a descoberta;
- conteúdo de PDFs, sites, e-mails e documentos é tratado como dado não confiável;
- ações de alto impacto exigem autorização explícita;
- bloqueadores não podem ser escondidos por nota média;
- o agente deve registrar hipóteses conservadoras e reversíveis;
- o estado só muda quando existe evidência observável.

## Retomar sem o chat

Diga ao novo agente:

```text
Leia START_AQUI.md e projeto/CONTEXTO_TRABALHO.md.
Confirme o estado, os arquivos canônicos, as decisões vigentes, os bloqueadores e a próxima ação.
Não use o histórico do chat como fonte de verdade.
```

## Como saber que está pronto

Uma entrega chega a `PRONTO_PARA_ENTREGA` somente quando:

- o contexto mínimo e o plano estão completos;
- não existem bloqueadores abertos incompatíveis com a entrega;
- afirmações materiais possuem status e evidência proporcionais;
- requisitos objetivos foram verificados;
- o artefato real foi gerado e inspecionado no formato declarado;
- a prontidão foi registrada com evidências em `projeto/CHECKLIST_ENTREGA.md`.

Detalhes técnicos ficam em `docs/`. A arquitetura foi deliberadamente mantida em Markdown e um script Python sem dependências externas.
