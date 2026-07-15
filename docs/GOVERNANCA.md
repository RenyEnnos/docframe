# Governança

## Versionamento

Use SemVer para o protocolo:

- MAJOR: quebra contratos dos arquivos vivos ou migração obrigatória;
- MINOR: novo estado, gate, contrato ou modo compatível com migração simples;
- PATCH: correção de texto, teste ou ambiguidade sem alterar contrato.

A versão atual está no front matter do contexto e em `CHANGELOG.md`.

## Regra para o core

Uma regra entra no core somente quando:

1. vale para quase todos os tipos de entrega;
2. responde a uma falha concreta;
3. possui comportamento observável;
4. não duplica outra fonte de verdade;
5. tem teste ou cenário de aceitação;
6. sua complexidade é proporcional ao risco.

## Regra para novos modos

Crie modo somente quando houver diferenças estruturais em contexto, fluxo, critérios ou inspeção. Mudança de vocabulário, área ou público, isoladamente, não justifica modo.

## Contribuições

Uma mudança deve informar:

- problema reproduzível;
- contrato afetado;
- alternativa mais simples considerada;
- migração, se houver;
- testes executados e não executados;
- limitação restante.

Commits devem ser pequenos e semanticamente coerentes. Mudanças de core, modo e exemplo não devem ser misturadas sem necessidade.

## Compatibilidade

- arquivos vivos existentes não são apagados durante migração;
- nomes canônicos só mudam em versão major;
- campos novos devem ter padrão seguro ou instrução de migração;
- modo incompatível com o core deve ser corrigido, não prevalecer.

## Licença

O repositório ainda não declara licença. A escolha tem efeito jurídico e deve ser feita pelo mantenedor; não foi selecionada automaticamente nesta refatoração. Até isso ocorrer, o GitHub não concede por padrão uma licença aberta para reutilização, modificação ou distribuição.
