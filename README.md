# End-to-End Sales Analytics Pipeline

Pipeline de analise de vendas em Python, cobrindo extracao, transformacao, criacao de features, metricas de negocio e exportacao dos resultados.

## Estrutura

- `data/raw`: arquivos CSV de entrada.
- `data/processed`: arquivos gerados pela execucao do pipeline.
- `src/extract`: leitura dos CSVs e padronizacao inicial das colunas.
- `src/transform`: limpeza, tratamento de datas e criacao de features.
- `src/pipeline`: orquestracao das transformacoes.
- `src/analytics`: metricas de negocio.
- `src/load`: salvamento dos resultados processados.
- `main.py`: ponto de entrada do projeto.

## Como Rodar

1. Instale as dependencias do projeto.
2. Coloque os arquivos CSV em `data/raw`.
3. Execute:

```bash
python main.py
```

Os arquivos processados serao gerados em `data/processed`.

## Metricas Geradas

- Top clientes por LTV.
- Top produtos por faturamento.
- Ranking de produtos por mes e ano.
- Classificacao ABC de produtos.
- Faturamento por classe ABC.
- Clientes em risco de churn.
- Produtos em risco de churn.
- Faturamento mensal.

## Observacoes

Arquivos gerados, caches Python e configuracoes locais de IDE ficam fora do versionamento via `.gitignore`.
