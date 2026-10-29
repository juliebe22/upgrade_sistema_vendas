from produtos import listar_produtos

print("\n--- PRIMEIRA CONSULTA ---")
produtos = listar_produtos()
print("Quantidade de produtos:", len(produtos))

print("\n--- SEGUNDA CONSULTA ---")
produtos = listar_produtos()
print("Quantidade de produtos:", len(produtos))
