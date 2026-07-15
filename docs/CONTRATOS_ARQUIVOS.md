# Contratos dos Arquivos

## Regra geral

Cada informação possui uma única fonte de verdade. Referências cruzadas usam IDs; não copie manualmente o mesmo estado para vários arquivos.

| Arquivo | Função exclusiva | Pode conter | Não deve conter | Atualização | Fonte de verdade |
|---|---|---|---|---|---|
| `projeto/CONTEXTO_TRABALHO.md` | estado e resumo canônico | objetivo, entrega, cobertura, módulos, bloqueadores, próxima ação, ponteiros | histórico detalhado, catálogo completo de fontes, notas extensas | toda transição ou mudança material | estado, escopo, formato, módulos, bloqueadores |
| `projeto/DECISOES.md` | decisões vigentes e substituídas | ID, decisão, motivo, autoridade, impacto, status | fatos externos sem origem, histórico narrativo | ao tomar/revogar decisão | decisões |
| `projeto/REFERENCIAS_CANDIDATAS.md` | catálogo de fontes | origem, localização, inspeção, confiabilidade, incorporação | texto final ou afirmação não decomposta | em cada busca/inspeção | fontes |
| `projeto/AFIRMACOES.md` | registro de afirmações materiais | tipo, origem, evidência, confiança, uso, validação | bibliografia completa, decisões de formato | ao produzir ou revisar afirmação | sustentação factual |
| `projeto/RUBRICA.md` | critérios de avaliação | critérios atômicos, âncoras, bloqueadores, evidência esperada | notas de uma iteração | na modelagem ou mudança de requisitos | critérios |
| `projeto/SCORECARD.md` | resultados de avaliação | resultado, evidência, confiança, lacuna, prioridade | redefinição silenciosa da rubrica | em cada avaliação | avaliações |
| `projeto/CHECKLIST_ENTREGA.md` | gates e requisitos objetivos | estado dos gates, evidência, responsável | notas holísticas ou narrativa longa | ao satisfazer/invalidar gate | conclusão objetiva |
| `projeto/BASE_CONHECIMENTO.md` | síntese operacional derivada | conceitos e dados referenciados por IDs | fatos sem ID de afirmação/fonte | quando síntese facilitar produção | síntese, nunca a origem |
| `projeto/REGISTRO_ITERACOES.md` | histórico cronológico curto | alterações, decisões referenciadas, testes, próxima ação | duplicação integral de arquivos vivos | fim de cada iteração material | ordem histórica |
| `projeto/logs/` | evidência detalhada excepcional | relatórios extensos, saídas de ferramentas | estado canônico único | quando o resumo seria insuficiente | detalhe, não estado |

## Quem pode atualizar

- agente: arquivos vivos, dentro da autonomia registrada;
- usuário: qualquer conteúdo do projeto e aprovações que lhe competem;
- autoridade externa: sua validação é registrada pelo agente, nunca presumida;
- core/modos/docs: somente manutenção do Docframe, não execução normal.

## Reconciliação

1. identifique a categoria em conflito;
2. aplique a fonte de verdade da tabela;
3. preserve a informação divergente como pendência ou decisão substituída quando necessário;
4. atualize referências cruzadas;
5. registre a reconciliação em `projeto/REGISTRO_ITERACOES.md`.
