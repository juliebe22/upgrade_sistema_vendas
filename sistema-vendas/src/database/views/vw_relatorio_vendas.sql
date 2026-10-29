CREATE OR REPLACE VIEW vw_relatorio_vendas AS
SELECT
    v.id_venda,
    v.data,
    p.nome AS produto,
    v.quantidade,
    p.preco AS preco_unitario,
    v.valor_total,
    v.forma_pagamento
FROM vendas v
INNER JOIN produtos p
    ON v.id_produto = p.id_produto
ORDER BY v.data DESC;