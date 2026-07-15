# Diagnóstico do Estado Inicial

Data da auditoria: 2026-07-14. Base auditada: `main` no commit `38c2c3e4b32d113a2b0251644b690478297236e1`.

## Resumo executivo

O Docframe já possuía princípios corretos — entrevista antes da escrita, separação entre hipótese e fato, carregamento seletivo de modos e declaração de prontidão —, mas dependia de o agente lembrar e interpretar regras espalhadas. Não havia máquina de estados, gate de contexto mínimo, contrato de fonte de verdade, registro próprio de afirmações, política explícita contra instruções em conteúdo externo nem testes executáveis.

## Mapa de problemas

| Impacto | Problema observado | Consequência | Correção adotada |
|---|---|---|---|
| crítico | `CHECKLIST_ENTREGA.md` exigia PDF para qualquer entrega | DOCX, Markdown, apresentação e outros artefatos jamais satisfaziam o critério de pronto | gate de entrega baseado no formato declarado |
| crítico | validação dependia de declaração do agente | item podia ser marcado como validado sem evidência | toda transição e avaliação exige evidência identificável |
| crítico | conteúdo externo não tinha política de confiança | PDF, site ou template podia tentar alterar o protocolo | política de conteúdo não confiável e autorização de alto impacto |
| alto | não havia fluxo explícito de estados | etapas podiam ser puladas ou encerradas por afirmação | estados, transições e gates G0–G6 |
| alto | `CONTEXTO_TRABALHO.md` duplicava decisões, fontes e afirmações | divergências entre arquivos vivos | fonte de verdade e ponteiros canônicos |
| alto | entrevista era lista fixa | perguntas repetidas e contexto mínimo indefinido | elicitação por cobertura, confiança e impacto |
| alto | fonte “validada” reunia várias decisões diferentes | fonte encontrada podia ser tratada como prova | cadeia de status: encontrada, inspecionada, confiável, incorporada e citada |
| alto | rubrica holística de 0 a 10 | nota escondia requisito obrigatório ausente | critérios atômicos, estados categóricos e bloqueadores independentes |
| médio | LaTeX aparecia como preferência universal do core | escolha de ferramenta antecedia a necessidade | formato final deliberado; LaTeX como módulo condicional |
| médio | core misturava invariantes e convenções acadêmicas | módulos irrelevantes eram carregados | manifesto de contexto e roteamento por risco/entrega |
| médio | retomada dependia do histórico da conversa | perda de decisões entre sessões | resumo canônico no arquivo mestre e rotina de retomada |
| médio | ausência de testes estáticos | caminhos, nomes antigos e contradições podiam regressar | script Python sem dependências e cenários de aceitação |
| médio | faltavam changelog, governança e migração | evolução sem contrato de compatibilidade | documentação de governança, migração e changelog |
| baixo | README concentrava regras demais | onboarding misturado com especificação | README curto com detalhes técnicos em `docs/` |

## Termos residuais encontrados

- o nome anterior estava presente no histórico e em decisões de renomeação.
- `TCC` aparecia principalmente como exemplo e como negação do pressuposto acadêmico.
- `LaTeX/PDF` e “PDF final” apareciam como defaults e gates universais.
- termos absolutos como “sempre”, “nunca” e “garantido” apareciam sem distinção entre invariantes e conteúdo a revisar.
- licença, changelog e convenções de contribuição não existiam.

## O que foi preservado

- Markdown como meio principal;
- estrutura `core/`, `agente/`, `modos/`, `projeto/` e `docs/`;
- primeiro uso por uma instrução curta;
- arquivos vivos legíveis por pessoas;
- logs híbridos;
- modos de currículo e proposta institucional;
- ausência de banco, servidor, nuvem ou runtime pesado.
