# Arquitetura do Docframe

O Docframe é um protocolo documental leve. Markdown guarda estado e contratos; um script opcional verifica invariantes estáticos. A arquitetura evita banco de dados, servidor, framework agentivo e dependência de fornecedor.

## Fontes de verdade

- estado e resumo de retomada: `projeto/CONTEXTO_TRABALHO.md`;
- decisões: `projeto/DECISOES.md`;
- fontes: `projeto/REFERENCIAS_CANDIDATAS.md`;
- afirmações: `projeto/AFIRMACOES.md`;
- critérios: `projeto/RUBRICA.md`;
- avaliações: `projeto/SCORECARD.md`;
- gates: `projeto/CHECKLIST_ENTREGA.md`;
- histórico: `projeto/REGISTRO_ITERACOES.md`;
- produto: caminho declarado como artefato final canônico no contexto.

Em conflito, vence a fonte de verdade da categoria. O arquivo divergente deve ser reconciliado na mesma iteração e o conflito registrado.

## Dez subsistemas

### 1. Entrada e descoberta da demanda

- finalidade: reconhecer objetivo, produto e estado atual;
- entradas obrigatórias: pedido do usuário e `projeto/CONTEXTO_TRABALHO.md`;
- opcionais: arquivos, links, histórico de projeto;
- saída: demanda extraída e estado `DESCOBERTA`;
- estado responsável: `projeto/CONTEXTO_TRABALHO.md`;
- entrada: bootstrap G0;
- saída: matriz de cobertura iniciada;
- bloqueadores: pedido vazio ou artefato alvo ambíguo;
- falha: começar a produzir por impulso;
- recuperação: registrar lacunas e perguntar apenas o bloqueador;
- evidência: entrada de transição;
- testes: C01, T01 e T04.

### 2. Elicitação adaptativa

- finalidade: atingir contexto suficiente sem questionário exaustivo;
- entradas obrigatórias: fatos já fornecidos e categorias de cobertura;
- opcionais: hipóteses conservadoras;
- saída: gate G1 atendido ou espera/bloqueio explícito;
- estado responsável: `projeto/CONTEXTO_TRABALHO.md`;
- entrada: `DESCOBERTA`;
- saída: objetivo, produto, público, canal/formato, materiais, autoridades, conclusão e autonomia cobertos;
- bloqueadores: lacuna material sem hipótese reversível;
- falha: repetir pergunta conhecida ou transformar “não sei” em fato;
- recuperação: extrair antes de perguntar, registrar confiança e impacto;
- evidência: tabela de cobertura;
- testes: C05 e T01.

### 3. Classificação e roteamento

- finalidade: carregar somente o core e os módulos relevantes;
- entradas obrigatórias: tipo de entrega, riscos e formato;
- opcionais: modo especializado;
- saída: módulos ativos e justificativa;
- estado responsável: `projeto/CONTEXTO_TRABALHO.md`;
- entrada: G1;
- saída: manifesto resolvido;
- bloqueadores: nenhum modo conhecido não é bloqueador;
- falha: carregar tudo ou inventar modo;
- recuperação: usar core genérico e registrar candidato futuro;
- evidência: tabela de módulos;
- testes: C12 e T07.

### 4. Montagem do contexto operacional

- finalidade: selecionar o menor conjunto suficiente de arquivos;
- entradas obrigatórias: estado e módulos ativos;
- opcionais: resumo canônico e material sob demanda;
- saída: conjunto de leitura da sessão;
- estado responsável: `agente/MANIFESTO_CONTEXTO.md` e contexto mestre;
- entrada: estado reconhecido;
- saída: arquivos obrigatórios, condicionais e descartados identificados;
- bloqueadores: arquivo canônico ausente;
- falha: despejar toda a documentação ou usar memória desatualizada;
- recuperação: recarregar resumo e somente os arquivos do estado;
- evidência: registro de retomada;
- testes: C10 e T07.

### 5. Planejamento do trabalho

- finalidade: converter a entrega em estrutura, unidades e critérios;
- entradas obrigatórias: contexto mínimo, rubrica e restrições;
- opcionais: exemplos, template e ordem sugerida;
- saída: plano verificável e gate G2;
- estado responsável: contexto, rubrica e checklist;
- entrada: `MODELAGEM`;
- saída: `PLANEJADO`;
- bloqueadores: requisito obrigatório incompatível;
- falha: escrever antes de modelar;
- recuperação: voltar a descoberta ou registrar decisão;
- evidência: plano confrontado com critérios;
- testes: C01 e C06.

### 6. Pesquisa, fontes e proveniência

- finalidade: ligar afirmações a origens inspecionadas;
- entradas obrigatórias: política de pesquisa e afirmações a sustentar;
- opcionais: termos de busca e fontes fornecidas;
- saída: cadeia de proveniência mínima e gate G3;
- estado responsável: referências e afirmações;
- entrada: `PESQUISA` ou demanda factual durante produção;
- saída: fonte, localização e status registrados;
- bloqueadores: evidência inacessível ou conflito material;
- falha: tratar fonte encontrada como prova integral;
- recuperação: inspecionar, decompor afirmação ou reduzir certeza;
- evidência: IDs cruzados de fonte e afirmação;
- testes: C04, C08 e T05.

### 7. Produção e revisão do conteúdo

- finalidade: produzir em unidades controláveis preservando escopo e voz;
- entradas obrigatórias: plano e contexto válidos;
- opcionais: estilo e modo específico;
- saída: artefato intermediário e afirmações extraídas;
- estado responsável: artefato e registro de iterações;
- entrada: `EM_PRODUCAO` após G2;
- saída: artefato verificável;
- bloqueadores: nova lacuna material;
- falha: alterar objetivo silenciosamente ou refinar infinitamente;
- recuperação: reabrir estado correto e aplicar condição de parada;
- evidência: diff/versão e iteração;
- testes: C03 e C05.

### 8. Avaliação e validação

- finalidade: separar checagens determinísticas, julgamento crítico e aprovação;
- entradas obrigatórias: artefato, rubrica e evidências;
- opcionais: avaliador independente ou humano;
- saída: scorecard, lacunas e gate G5;
- estado responsável: `projeto/SCORECARD.md`;
- entrada: `EM_VERIFICACAO`;
- saída: retorno à produção, revisão ou entrega;
- bloqueadores: requisito crítico não atendido;
- falha: autoindulgência ou média que esconde bloqueador;
- recuperação: papéis separados, critérios atômicos e evidência por item;
- evidência: registro de avaliação;
- testes: C03, C08 e T06.

### 9. Geração e inspeção do artefato

- finalidade: validar o produto real, não apenas seu texto fonte;
- entradas obrigatórias: formato declarado e artefato gerado;
- opcionais: ferramentas de renderização e template;
- saída: artefato canônico inspecionado;
- estado responsável: contexto e checklist;
- entrada: produção concluída;
- saída: G5/G6;
- bloqueadores: arquivo corrompido, formato incorreto ou inspeção impossível;
- falha: considerar formatação validada sem abrir/renderizar;
- recuperação: regenerar, trocar stack ou registrar limitação;
- evidência: comando, hash, captura ou relatório de inspeção;
- testes: C02, C11 e T03.

### 10. Persistência, retomada e encerramento

- finalidade: sobreviver à troca de sessão, modelo ou IDE;
- entradas obrigatórias: estado, próxima ação, decisões, bloqueadores e versão canônica;
- opcionais: log detalhado;
- saída: resumo retomável ou encerramento justificado;
- estado responsável: contexto e registro de iterações;
- entrada: qualquer estado;
- saída: retomada no estado correto ou `ENCERRADO`;
- bloqueadores: arquivos vivos contraditórios;
- falha: depender do chat;
- recuperação: reconciliar fontes de verdade e registrar reabertura;
- evidência: bloco “próxima ação” e transição;
- testes: C07 e C10.

## Fluxo resumido

`NAO_INICIADO → DESCOBERTA → CONTEXTO_MINIMO → MODELAGEM → (PESQUISA) → PLANEJADO → EM_PRODUCAO → EM_VERIFICACAO → PRONTO_PARA_REVISAO/PRONTO_PARA_ENTREGA → ENCERRADO`.

`AGUARDANDO_USUARIO` e `BLOQUEADO` são estados laterais. Mudança material pode retornar a descoberta, pesquisa, produção ou verificação.
