import sqlite3

DB_PATH = "support.db"

def inicializar_base_datos(db_path: str = DB_PATH):
    conn = sqlite3.connect(db_path)
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

def listar_pedidos_db(db_path: str = DB_PATH):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()
    
    conn.close()
    return pedidos

def insertar_pedido(estado: str, total: float, db_path: str = DB_PATH):
    conn = sqlite3.connect(db_path)
    
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

def buscar_pedido_db(id_pedido: int, db_path: str = DB_PATH):
    conn = sqlite3.connect(db_path)
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

def actualizar_estado_pedido_db(id_pedido: int, estado: str, db_path: str = DB_PATH):
    conn = sqlite3.connect(db_path)
    
    try:
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE pedidos SET estado=? WHERE id=?", (estado, id_pedido,)
        )
        rows = cursor.rowcount
        conn.commit()
        
        return rows
    
    except sqlite3.Error:
        conn.rollback()
        raise

    finally:
        conn.close()

def eliminar_pedido_db(id_pedido: str, db_path: str = DB_PATH):
    conn = sqlite3.connect(db_path)
    
    try:
        cursor = conn.cursor()
        cursor.execute(
            "DELTE FROM pedidos WHERE id=?", (id_pedido,)
        )
        rows = cursor.rowcount
        conn.commit()
        return rows
    
    except sqlite3.Error:
        conn.rollback()
        raise
    
    finally:
        conn.close()
    
if __name__ == "__main__":
    inicializar_base_datos()
