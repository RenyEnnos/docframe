# Guia de Migração para o Protocolo 0.2

## Objetivo

Migrar projetos anteriores sem apagar decisões válidas nem exigir reinício.

## Passos

1. faça cópia ou commit do projeto existente;
2. substitua arquivos de `core/`, `agente/` e `docs/` pela versão 0.2;
3. preserve o conteúdo dos arquivos vivos antigos;
4. migre o estado para o front matter de `projeto/CONTEXTO_TRABALHO.md`;
5. mova decisões para `projeto/DECISOES.md`;
6. decomponha afirmações materiais em `projeto/AFIRMACOES.md`;
7. mantenha fontes em `projeto/REFERENCIAS_CANDIDATAS.md`, convertendo os status;
8. adapte rubrica e checklist aos novos valores permitidos;
9. registre caminhos de artefatos e a versão canônica;
10. execute `python tests/check_docframe.py`;
11. registre a migração como iteração.

## Conversão de status de fontes

| Antigo | Novo |
|---|---|
| buscar | `BUSCAR` |
| encontrada | `ENCONTRADA` |
| validada | separar em `INSPECIONADA` e `CONFIAVEL` |
| incorporada | `INCORPORADA`; registrar também citação e sustentação |
| descartada | `DESCARTADA` com motivo |

## Conversão de prontidão

- “pronto” sem qualificador → `NAO_AVALIADA` até executar gates;
- “pronto para revisão” → `PRONTO_PARA_REVISAO` se houver artefato identificável;
- “pronto para entrega” → somente após G6;
- projeto interrompido → estado real da etapa ou `BLOQUEADO`/`AGUARDANDO_USUARIO`.

## Compatibilidade

Modos antigos continuam úteis como orientação, mas seus checklists não vencem o core. Qualquer exigência universal de PDF/LaTeX deve ser substituída pelo formato declarado no contexto.
