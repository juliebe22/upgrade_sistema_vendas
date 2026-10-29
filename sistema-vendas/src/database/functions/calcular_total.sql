CREATE OR REPLACE FUNCTION calcular_total(
    p_preco NUMERIC,
    p_quantidade INTEGER
)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN p_preco * p_quantidade;
END;
$$;