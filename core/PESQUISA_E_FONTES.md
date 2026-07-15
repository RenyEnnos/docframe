# Pesquisa, Afirmações e Proveniência

Use este módulo quando a entrega depender de informação externa ou de materiais fornecidos.

## Ciclo da fonte

Uma fonte percorre estados distintos:

`buscar` → `encontrada` → `inspecionada` → `confiavel_para_uso` → `incorporada` → `citacao_conferida`

Também pode ser `descartada`. Nenhum estado é inferido automaticamente do anterior.

## Registro mínimo da fonte

Em `projeto/REFERENCIAS_CANDIDATAS.md`, registre:

- identificador estável;
- título e origem;
- link, caminho, DOI ou hash;
- tipo de fonte;
- data e responsável pela inspeção;
- trecho, página, seção ou localização relevante;
- avaliação de confiabilidade e aplicabilidade;
- afirmações ligadas;
- local de uso;
- status e motivo de descarte, quando houver.

## Registro mínimo da afirmação

Em `projeto/AFIRMACOES.md`, registre:

- ID;
- texto ou resumo atômico;
- tipo: fato externo, declaração do usuário, dado fornecido, inferência, hipótese ou requisito institucional;
- origem;
- localização da evidência;
- confiança;
- status de validação;
- onde foi usada;
- responsável;
- última verificação.

Divida frases complexas quando uma única citação não sustentar todos os seus componentes.

## Proveniência mínima

- entidade: fonte, arquivo, dado, afirmação ou artefato;
- atividade: busca, inspeção, cálculo, revisão, transformação ou aprovação;
- agente: pessoa, modelo, ferramenta ou instituição;
- derivação: qual entidade e atividade originaram a saída.

Não é necessário RDF ou banco de dados; IDs e links internos são suficientes.

## Qualidade da citação

Avalie separadamente:

- correção: a fonte apoia a afirmação?
- completude: todas as partes materiais estão apoiadas?
- qualidade: a fonte é adequada ao contexto?
- posição: a citação está ligada à afirmação correta?

## Revisão factual

1. extraia afirmações materiais;
2. classifique cada uma;
3. procure ou inspecione evidência;
4. revise ou reduza afirmações não sustentadas;
5. preserve a intenção e a voz quando corrigir;
6. registre conflitos e limitações.
