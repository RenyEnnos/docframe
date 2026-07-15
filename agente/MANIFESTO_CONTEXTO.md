# Manifesto de Contexto

Este arquivo define carregamento progressivo.

## Ler sempre

- `core/REGRAS_FIXAS.md`;
- `core/PROTOCOLO_ESTADOS.md`;
- `agente/PROMPT_AGENTE.md`;
- `projeto/CONTEXTO_TRABALHO.md`.

## Ler por estado

| Estado | Arquivos adicionais |
|---|---|
| `DESCOBERTA` | `agente/ENTREVISTA_INICIAL.md` e `agente/ROTEAMENTO_MODOS.md` |
| `MODELAGEM` ou `PLANEJADO` | `projeto/RUBRICA.md`, `projeto/CHECKLIST_ENTREGA.md`, `projeto/DECISOES.md` |
| `PESQUISA` | `core/PESQUISA_E_FONTES.md`, `projeto/REFERENCIAS_CANDIDATAS.md`, `projeto/AFIRMACOES.md` |
| `EM_PRODUCAO` | plano, artefato canônico e módulos ativos |
| `EM_VERIFICACAO` | `core/VALIDACAO_E_ENTREGA.md`, rubrica, checklist, scorecard e artefato real |
| retomada | contexto mestre, decisões vigentes, bloqueadores e última iteração |

## Ler por modo

Carregue somente os modos registrados como ativos no contexto. Módulos não ativos não devem ser incluídos “por precaução”.

## Ler sob demanda

- histórico detalhado em `projeto/logs/`;
- referências descartadas;
- versões antigas;
- documentação de manutenção em `docs/`.

## Resumo canônico

`projeto/CONTEXTO_TRABALHO.md` é o resumo canônico de retomada. Se logs ou chat divergirem, o contexto vence até que uma reconciliação seja registrada em `projeto/DECISOES.md`.

## Desatualização

Qualquer arquivo derivado deve indicar a data e a origem. Quando estiver desatualizado, marque-o como tal; não mantenha duas versões vivas concorrentes.
