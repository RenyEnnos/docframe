# Referências de Projeto

Este documento registra somente referências que alteraram uma decisão do Docframe. A presença aqui não declara conformidade integral com nenhuma norma.

| Referência | Problema observado | Princípio extraído | Decisão resultante | Arquivos afetados | Adoção ou rejeição |
|---|---|---|---|---|---|
| Anthropic, *Building Effective Agents* (2024) — https://www.anthropic.com/engineering/building-effective-agents | regras extensas sem controle entre etapas | usar padrões simples, prompt chaining com gates, routing e ground truth; limitar iterações | estados G0–G6, roteamento e condições de parada | `core/PROTOCOLO_ESTADOS.md`, `agente/ROTEAMENTO_MODOS.md`, `core/VALIDACAO_E_ENTREGA.md` | adotado; framework agentivo pesado rejeitado |
| Wang et al., *Plan-and-Solve Prompting* (2023) — https://arxiv.org/abs/2305.04091 | produção começava antes de plano verificável | separar planejamento de execução | gate G2 antes de `EM_PRODUCAO` | protocolo de estados e checklist | adotado em forma mínima |
| Madaan et al., *Self-Refine* (2023) — https://arxiv.org/abs/2303.17651 | revisão sem ciclo controlado | gerar, avaliar, corrigir; não repetir sem critério | lista priorizada de lacunas e parada explícita | validação e scorecard | adotado; loop aberto rejeitado |
| Liu et al., *Lost in the Middle* (2023/2024) — https://arxiv.org/abs/2307.03172 | toda documentação era carregada de uma vez | selecionar e posicionar contexto relevante | manifesto por estado e resumo canônico | `agente/MANIFESTO_CONTEXTO.md`, contexto mestre | adotado |
| Liu et al., *G-Eval* (2023) — https://arxiv.org/abs/2303.16634 | notas holísticas sem evidência | critérios explícitos e avaliação estruturada | critérios atômicos e justificativa por evidência | rubrica e scorecard | adotado com verificações determinísticas separadas |
| Hashemi et al., *LLM-Rubric* (2024) — https://arxiv.org/abs/2309.08124 | rubrica genérica não capturava dimensões específicas | descrever atributos observáveis e calibráveis | escala curta e adaptada à entrega | rubrica | adotado sem exigir modelo específico |
| trabalhos sobre vieses de LLM-as-a-judge | mesmo modelo podia favorecer o próprio texto | separar produtor, verificador, avaliador e aprovador; não confiar em nota isolada | papéis e bloqueadores independentes | validação e scorecard | adotado; “juiz único” rejeitado como garantia |
| Gao et al., *RARR* (2023) — https://arxiv.org/abs/2210.08726 | texto podia ser revisado sem rastrear evidência | pesquisar atribuição e revisar preservando o conteúdo útil | afirmações materiais ligadas a evidência e revisão proporcional | pesquisa, afirmações e referências | adotado parcialmente, sem pipeline automatizado |
| Gao et al., *ALCE* (2023) — https://arxiv.org/abs/2305.14627 | citação próxima era tratada como sustentação suficiente | avaliar correção, completude e qualidade de citações separadamente | status distintos para fonte, incorporação, citação e sustentação | pesquisa, referências, afirmações | adotado |
| Min et al., *FActScore* (2023) — https://arxiv.org/abs/2305.14251 | parágrafos eram tratados como unidade factual | decompor texto em afirmações verificáveis | `projeto/AFIRMACOES.md` | afirmações e validação | adotado conceitualmente; pontuação automatizada rejeitada |
| W3C, *PROV-O* (2013) — https://www.w3.org/TR/prov-o/ | origem, atividade e responsável não eram ligados | entidade, atividade, agente e derivação como vocabulário mínimo | IDs de fonte, afirmação, decisão, iteração e responsável | contratos, referências e afirmações | adotado sem RDF/ontologia executável |
| NIST AI 600-1, *Generative AI Profile* (2024) — https://doi.org/10.6028/NIST.AI.600-1 | riscos e governança de IA eram implícitos | governar, mapear, medir e gerenciar; registrar proveniência, testes e incidentes/limitações | gates, segurança e relatório de limitações | regras, segurança, validação | adotado como orientação; conformidade não declarada |
| ISO/IEC/IEEE 29148:2018 — https://www.iso.org/standard/72089.html | necessidade, restrição, preferência e decisão eram misturadas | elicitar, analisar, especificar e validar requisitos com rastreabilidade | categorias de cobertura e critérios observáveis | entrevista, contexto, rubrica | adotado conceitualmente; texto integral não auditado e conformidade não declarada |
| Greshake et al., *More than you've asked for* (2023) — https://arxiv.org/abs/2302.12173 | documentos externos podiam conter instruções | separar instruções confiáveis de dados não confiáveis e limitar ações | política de conteúdo externo e autorização de alto impacto | segurança e regras fixas | adotado; detecção por palavras-chave rejeitada como única defesa |

## Limites da pesquisa

- A ISO/IEC/IEEE 29148 é protegida e não foi auditada integralmente; foi usada apenas como orientação conceitual a partir da descrição pública e literatura correlata.
- O Docframe não implementa métricas automáticas de ALCE, FActScore, G-Eval ou LLM-Rubric.
- Os padrões foram traduzidos para contratos Markdown simples; não há alegação de equivalência formal aos sistemas de pesquisa.
