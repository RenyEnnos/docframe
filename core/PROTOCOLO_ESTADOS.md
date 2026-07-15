# Protocolo de Estados

O estado canônico está no front matter de `projeto/CONTEXTO_TRABALHO.md`.

## Estados válidos

| Estado | Entrada | Permitido | Proibido | Evidência de saída | Próximos estados |
|---|---|---|---|---|---|
| `NAO_INICIADO` | projeto criado | ler núcleo e estado | produzir entrega | bootstrap registrado | `DESCOBERTA` |
| `DESCOBERTA` | demanda identificada | extrair contexto, perguntar, catalogar materiais | escrever entrega final | matriz de cobertura atualizada | `CONTEXTO_MINIMO`, `AGUARDANDO_USUARIO`, `BLOQUEADO` |
| `CONTEXTO_MINIMO` | G1 atendido | rotear e modelar | omitir lacuna bloqueadora | checklist G1 e módulos registrados | `MODELAGEM`, `PESQUISA`, `AGUARDANDO_USUARIO` |
| `MODELAGEM` | produto e restrições conhecidos | definir plano, rubrica e checklist | produzir sem estrutura aprovada | plano e critérios atômicos | `PESQUISA`, `PLANEJADO`, `DESCOBERTA` |
| `PESQUISA` | política de pesquisa definida | buscar, inspecionar e registrar fontes | usar fonte não inspecionada como prova | fontes e afirmações ligadas | `PLANEJADO`, `MODELAGEM`, `BLOQUEADO` |
| `PLANEJADO` | G2 atendido | iniciar produção em unidades | alterar objetivo silenciosamente | plano verificado contra contexto e rubrica | `EM_PRODUCAO`, `DESCOBERTA` |
| `EM_PRODUCAO` | plano e contexto válidos | produzir, revisar e registrar afirmações | declarar prontidão final | unidades produzidas e rastreadas | `EM_VERIFICACAO`, `PESQUISA`, `BLOQUEADO` |
| `EM_VERIFICACAO` | artefato verificável existente | executar testes, inspeção e avaliação | validar por declaração | relatório de evidências e lacunas | `EM_PRODUCAO`, `PRONTO_PARA_REVISAO`, `PRONTO_PARA_ENTREGA`, `BLOQUEADO` |
| `AGUARDANDO_USUARIO` | decisão ou dado do usuário necessário | trabalho preparatório reversível | presumir decisão material | pergunta e impacto registrados | estado anterior, `BLOQUEADO` |
| `BLOQUEADO` | impedimento técnico, factual ou institucional | registrar recuperação e alternativas | ocultar ou contornar bloqueador | bloqueador resolvido ou aceito por autoridade | estado anterior, `ENCERRADO` |
| `PRONTO_PARA_REVISAO` | artefato coerente para leitura | receber feedback e reabrir etapa | chamar de entrega final | escopo de revisão declarado | `EM_PRODUCAO`, `EM_VERIFICACAO`, `PRONTO_PARA_ENTREGA` |
| `PRONTO_PARA_ENTREGA` | G6 atendido | entregar artefato identificado | manter bloqueador incompatível | artefato inspecionado e checklist completo | `ENCERRADO`, `EM_PRODUCAO` |
| `ENCERRADO` | entrega concluída ou encerramento justificado | arquivar resumo e limitações | continuar alterando sem reabertura | motivo e versão canônica registrados | `DESCOBERTA` por reabertura explícita |

## Gates

### G0 — bootstrap

- núcleo lido;
- estado reconhecido;
- fonte de verdade identificada.

### G1 — contexto mínimo

- objetivo, produto, público, formato/canal, materiais, autoridades, critério de conclusão e autonomia estão cobertos, não aplicáveis ou registrados como hipótese reversível;
- nenhuma lacuna bloqueadora impede modelagem.

### G2 — planejamento

- escopo e fora de escopo definidos;
- plano ou estrutura verificável;
- rubrica adaptada;
- checklist adaptado;
- dependências e bloqueadores conhecidos.

### G3 — pesquisa e proveniência

- política de pesquisa definida;
- fontes usadas estão inspecionadas;
- afirmações materiais possuem origem, localização e status;
- conflitos de fonte estão registrados.

### G4 — produção

- unidades produzidas correspondem ao plano;
- novas afirmações foram registradas;
- mudanças materiais reabriram a etapa correta.

### G5 — verificação

- verificações determinísticas executadas;
- avaliação subjetiva baseada em critérios e evidências;
- artefato real inspecionado;
- lacunas priorizadas e motivo de parada registrado.

### G6 — entrega

- formato e versão canônica identificados;
- bloqueadores incompatíveis fechados;
- requisitos obrigatórios atendidos;
- prontidão declarada com evidência;
- limitações restantes comunicadas.

## Transição

Toda transição deve registrar: estado anterior, estado novo, gate, evidências, agente ou pessoa responsável, data e condição de reabertura.
