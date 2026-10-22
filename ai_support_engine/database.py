import sqlite3

DB_PATH = "support.db"

def inicializar_base_datos():
    conn = sqlite3.connect(DB_PATH)
    print("Conexión con la db establecida")

    cursor = conn.cursor()

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS pedidos (
                    id INTEGER PRIMARY KEY,
                    estado TEXT NOT NULL,
                    total REAL NOT NULL CHECK (total >= 0)
                )
    """)
    
    conn.commit()
    conn.close()

def listar_pedidos_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()
    
    conn.close()
    return pedidos

def insertar_pedido(estado: str, total: float):
    conn = sqlite3.connect(DB_PATH)
    
    try:
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO pedidos (estado, total)VALUES (? , ?)", (estado, total))
        
        last_id = cursor.lastrowid
        
        conn.commit()
        return last_id
    except sqlite3.Error:
        conn.rollback()
        raise
    finally:
        conn.close()

def buscar_pedido_db(id_pedido: int):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pedidos WHERE id =?", (id_pedido,))
        pedido = cursor.fetchone()
        if pedido == None:
            return None
        
        pedido_dict = dict(pedido)
    finally:
        conn.close()
    return pedido_dict


    

if __name__ == "__main__":
    inicializar_base_datos()
