# Start Aqui

Este é o ponto de entrada do Docframe.

## Instrução curta

```text
Leia o protocolo do Docframe, identifique o estado atual e conduza o próximo passo necessário.
```

## Bootstrap obrigatório

1. Leia `core/REGRAS_FIXAS.md`.
2. Leia `core/PROTOCOLO_ESTADOS.md`.
3. Leia `agente/PROMPT_AGENTE.md`.
4. Leia `projeto/CONTEXTO_TRABALHO.md`.
5. Use `agente/MANIFESTO_CONTEXTO.md` para carregar somente o necessário.
6. Verifique o gate do estado atual antes de executar a próxima etapa.

Não carregue todos os módulos por reflexo. Não comece a entrega final porque “parece haver contexto suficiente”. A transição precisa indicar evidência observável.

## Primeira resposta do agente

Em poucas linhas, informe:

- estado identificado;
- objetivo e produto final, quando conhecidos;
- lacunas de maior impacto;
- próximo passo permitido pelo protocolo.

O usuário pode responder “não sei”. Registre a lacuna, adote hipótese conservadora e reversível quando possível e prossiga até encontrar um bloqueador real.

## Retomada

Em uma nova sessão, o agente deve considerar `projeto/CONTEXTO_TRABALHO.md` a fonte de verdade do estado. Logs e chat servem como evidência auxiliar, nunca como estado canônico.
