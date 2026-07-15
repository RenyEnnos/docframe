# Validação e Entrega

## Separação de verificações

### Determinísticas

Use ferramentas ou checagens objetivas para:

- existência de arquivo e caminho;
- campos obrigatórios;
- estados e valores permitidos;
- links internos;
- compilação ou geração;
- fórmulas e totais;
- formato, tamanho e estrutura;
- presença de evidência em item marcado como validado.

### Subjetivas

Use rubrica atômica e ancorada para clareza, coerência, adequação, argumentação, legibilidade e qualidade visual.

## Escala

Cada critério deve usar um destes resultados:

- `ATENDE`;
- `NAO_ATENDE`;
- `NAO_AVALIADO`;
- `NAO_APLICAVEL`.

Qualidade gradual pode usar escala de 1 a 4 com âncoras explícitas. Toda avaliação exige evidência e confiança.

## Bloqueadores

Uma nota alta não compensa:

- fonte inventada;
- requisito obrigatório ausente;
- dado contraditório não resolvido;
- artefato corrompido;
- formato final incorreto;
- bloqueador institucional;
- ausência de autorização necessária.

## Inspeção por artefato

- DOCX: estilos, estrutura, campos, compatibilidade e inspeção visual;
- PDF: renderização, margens, paginação, figuras e fontes;
- LaTeX: compilação, referências e PDF gerado quando esse for o produto;
- Markdown: links, hierarquia e renderização;
- HTML/CSS: renderização, responsividade e acessibilidade aplicável;
- apresentação: narrativa, legibilidade, proporção e exportação;
- planilha: fórmulas, tipos, unidades, validações e abertura;
- formulário ou e-mail: campos, limites, destinatário e texto final.

## Prontidão

- `PRONTO_PARA_REVISAO`: pode ser avaliado pelo usuário ou terceiro, mas ainda há confirmação ou ajuste esperado;
- `PRONTO_PARA_ENTREGA`: requisitos e gates de entrega atendidos, artefato real inspecionado e bloqueadores incompatíveis fechados;
- `ENCERRADO_COM_LIMITACOES`: trabalho termina com impedimentos explicitamente documentados.

## Refinamento e parada

Após cada avaliação, produza lacunas priorizadas. Corrija somente lacunas confirmadas. Pare por critérios atendidos, limite de iteração, melhoria marginal, falta de evidência, decisão humana ou bloqueio. Registre o motivo.
