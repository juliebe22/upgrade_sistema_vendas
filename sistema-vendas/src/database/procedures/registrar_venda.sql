CREATE OR REPLACE PROCEDURE registrar_venda(
    p_id_produto INTEGER,
    p_quantidade INTEGER,
    p_forma_pagamento VARCHAR(30)
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_preco NUMERIC(10,2);
    v_estoque INTEGER;
    v_total NUMERIC(10,2);
    v_nome_produto VARCHAR(100);
BEGIN

    SELECT nome, preco, estoque
    INTO v_nome_produto, v_preco, v_estoque
    FROM produtos
    WHERE id_produto = p_id_produto;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Produto não encontrado.';
    END IF;

    IF p_quantidade <= 0 THEN
        RAISE EXCEPTION 'A quantidade deve ser maior que zero.';
    END IF;

    IF v_estoque < p_quantidade THEN
        RAISE EXCEPTION 'Estoque insuficiente.';
    END IF;

    v_total := calcular_total(v_preco, p_quantidade);

    INSERT INTO vendas (
        id_produto,
        quantidade,
        valor_total,
        forma_pagamento
    )
    VALUES (
        p_id_produto,
        p_quantidade,
        v_total,
        p_forma_pagamento
    );

    UPDATE produtos
    SET estoque = estoque - p_quantidade
    WHERE id_produto = p_id_produto;

    INSERT INTO movimentacoes (
        tipo,
        descricao,
        valor
    )
    VALUES (
        'ENTRADA',
        'Venda de ' || p_quantidade || ' unidade(s) de ' || v_nome_produto,
        v_total
    );

END;
$$;