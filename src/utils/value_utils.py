def format_value(valor):
    try:
        if isinstance(valor, (int, float)):
            return f"{valor:.2f}".replace(".", ",")

        if isinstance(valor, str):
            if "," in valor:
                partes = valor.split(",")
                if len(partes[1]) == 1:
                    return f"{partes[0]},{partes[1]}0"
                return valor

            return f"{valor},00"

        return valor
    except Exception as e:
        print(f"Erro na funcao format_value. Reinicie a aplicacao: {e}")
        return valor
