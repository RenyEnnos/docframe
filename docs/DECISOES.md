# Decisões do Framework

Registro curto de decisões arquiteturais do Infrakit Cru.

## 2026-05-21 - Separar núcleo fixo de arquivos vivos

O Infrakit foi dividido em `core/`, `agente/`, `projeto/` e `docs/`.

Motivo: permitir que o agente adapte o trabalho sem modificar as regras permanentes do framework.

## 2026-05-21 - Manter LaTeX como padrão forte

LaTeX é o padrão para documentos acadêmicos e técnicos formais, salvo exigência formal diferente ou modo específico com formato mais adequado.

Motivo: preservar compilação reprodutível, controle de referências e formatação acadêmica.

## 2026-05-21 - Usar logs híbridos

O registro principal fica em `projeto/REGISTRO_ITERACOES.md`, e detalhes longos vão para `projeto/logs/`.

Motivo: manter histórico navegável sem perder evidência de iterações grandes.

## 2026-05-21 - Não assumir TCC como padrão

O agente deve entrevistar o usuário antes de adaptar a rubrica e checklist.

Motivo: o mesmo framework deve servir para TCC, artigo, relatório, seminário, revisão bibliográfica e outros tipos de entrega.

## 2026-05-21 - Adicionar modos sem carregar tudo por padrão

Modos específicos passaram a viver em `modos/`, acionados por `agente/ROTEAMENTO_MODOS.md`.

Motivo: permitir propostas institucionais/técnicas sem transformar todo trabalho simples em fluxo burocrático.

## 2026-05-21 - Separar escrito, validado e pronto

O protocolo `core/VALIDACAO_E_ENTREGA.md` classifica níveis de verdade, promessas fortes e status de prontidão.

Motivo: evitar que texto bem escrito seja confundido com fato validado ou entrega final.

## 2026-05-21 - Tratar LaTeX como padrão, não imposição universal

LaTeX segue como padrão para documentos acadêmicos e técnicos formais, mas modos específicos podem declarar outra stack de saída quando o canal real exigir, como PDF/DOCX de currículo gerado por HTML/CSS.

Motivo: preservar reprodutibilidade sem forçar uma ferramenta inadequada para currículos, documentação web-first ou pipelines já existentes.

## 2026-05-21 - Adiar CLI e separação completa de templates

O feedback sobre `infrakit init`, `core/formats/` e isolamento total dos arquivos do usuário é válido, mas não foi implementado nesta etapa.

Motivo: isso muda a arquitetura de distribuição do projeto. Antes de criar CLI ou mover `projeto/` para uma área gerada/ignorada, o fluxo precisa ser testado em mais casos reais.
