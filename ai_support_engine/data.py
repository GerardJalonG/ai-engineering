# ai_support_engine/data.py

pedidos = [
    {
        "id": 1001,
        "cliente": {"id": 1, "nombre": "Carlos Martínez", "email": "carlos@example.com"},
        "estado": "pendiente",
        "fecha": "2026-10-01",
        "productos": [
            {"sku": "TEC-001", "nombre": "Teclado mecánico", "cantidad": 1, "precio": 65.90},
            {"sku": "TEC-002", "nombre": "Ratón inalámbrico", "cantidad": 1, "precio": 29.90}
        ],
        "total": 95.80,
        "metodo_pago": "tarjeta",
        "direccion_envio": {"ciudad": "Barcelona", "codigo_postal": "08001"},
        "notas": None
    },
    {
        "id": 1002,
        "cliente": {"id": 2, "nombre": "Laura Gómez", "email": "laura@example.com"},
        "estado": "enviado",
        "fecha": "2026-10-02",
        "productos": [
            {"sku": "INF-001", "nombre": "Monitor 27 pulgadas", "cantidad": 2, "precio": 189.99}
        ],
        "total": 379.98,
        "metodo_pago": "paypal",
        "direccion_envio": {"ciudad": "Madrid", "codigo_postal": "28001"},
        "notas": "Entregar por la mañana"
    },
    {
        "id": 1003,
        "cliente": {"id": 3, "nombre": "David López", "email": "david@example.com"},
        "estado": "entregado",
        "fecha": "2026-10-03",
        "productos": [
            {"sku": "ACC-001", "nombre": "Cable USB-C", "cantidad": 3, "precio": 12.50}
        ],
        "total": 37.50,
        "metodo_pago": "tarjeta",
        "direccion_envio": {"ciudad": "Valencia", "codigo_postal": "46001"},
        "notas": None
    },
    {
        "id": 1004,
        "cliente": {"id": 4, "nombre": "Marta Fernández", "email": "marta@example.com"},
        "estado": "cancelado",
        "fecha": "2026-10-04",
        "productos": [
            {"sku": "AUD-001", "nombre": "Auriculares Bluetooth", "cantidad": 1, "precio": 89.90}
        ],
        "total": 89.90,
        "metodo_pago": "tarjeta",
        "direccion_envio": {"ciudad": "Sevilla", "codigo_postal": "41001"},
        "notas": "Cancelado por el cliente"
    },
    {
        "id": 1005,
        "cliente": {"id": 5, "nombre": "Javier Ruiz", "email": "javier@example.com"},
        "estado": "pendiente",
        "fecha": "2026-10-05",
        "productos": [
            {"sku": "INF-002", "nombre": "SSD NVMe 1TB", "cantidad": 1, "precio": 79.99},
            {"sku": "ACC-002", "nombre": "Adaptador USB-C", "cantidad": 2, "precio": 15.00}
        ],
        "total": 109.99,
        "metodo_pago": "transferencia",
        "direccion_envio": {"ciudad": "Zaragoza", "codigo_postal": "50001"},
        "notas": None
    },
    {
        "id": 1006,
        "cliente": {"id": 6, "nombre": "Ana Torres", "email": "ana@example.com"},
        "estado": "preparacion",
        "fecha": "2026-10-06",
        "productos": [
            {"sku": "TEC-003", "nombre": "Webcam Full HD", "cantidad": 1, "precio": 54.90}
        ],
        "total": 54.90,
        "metodo_pago": "paypal",
        "direccion_envio": {"ciudad": "Bilbao", "codigo_postal": "48001"},
        "notas": "Pedido urgente"
    },
    {
        "id": 1007,
        "cliente": {"id": 7, "nombre": "Sergio Romero", "email": "sergio@example.com"},
        "estado": "entregado",
        "fecha": "2026-10-07",
        "productos": [
            {"sku": "INF-003", "nombre": "Portátil 15 pulgadas", "cantidad": 1, "precio": 899.00},
            {"sku": "ACC-003", "nombre": "Mochila para portátil", "cantidad": 1, "precio": 39.90}
        ],
        "total": 938.90,
        "metodo_pago": "tarjeta",
        "direccion_envio": {"ciudad": "Málaga", "codigo_postal": "29001"},
        "notas": None
    },
    {
        "id": 1008,
        "cliente": {"id": 8, "nombre": "Paula Sánchez", "email": "paula@example.com"},
        "estado": "pendiente",
        "fecha": "2026-10-08",
        "productos": [
            {"sku": "AUD-002", "nombre": "Altavoz Bluetooth", "cantidad": 2, "precio": 49.95}
        ],
        "total": 99.90,
        "metodo_pago": "bizum",
        "direccion_envio": {"ciudad": "Girona", "codigo_postal": "17001"},
        "notas": None
    },
    {
        "id": 1009,
        "cliente": {"id": 9, "nombre": "Miguel Navarro", "email": "miguel@example.com"},
        "estado": "enviado",
        "fecha": "2026-10-09",
        "productos": [
            {"sku": "INF-004", "nombre": "Memoria RAM 32GB", "cantidad": 2, "precio": 85.00}
        ],
        "total": 170.00,
        "metodo_pago": "tarjeta",
        "direccion_envio": {"ciudad": "Tarragona", "codigo_postal": "43001"},
        "notas": None
    },
    {
        "id": 1010,
        "cliente": {"id": 10, "nombre": "Elena Castro", "email": "elena@example.com"},
        "estado": "pendiente",
        "fecha": "2026-10-10",
        "productos": [
            {"sku": "TEC-004", "nombre": "Hub USB-C", "cantidad": 1, "precio": 35.50}
        ],
        "total": 35.50,
        "metodo_pago": "tarjeta",
        "direccion_envio": {"ciudad": "Alicante", "codigo_postal": "03001"},
        "notas": None
    },
    {
        "id": 1011,
        "cliente": {"id": 11, "nombre": "Rubén Díaz", "email": "ruben@example.com"},
        "estado": "preparacion",
        "fecha": "2026-10-11",
        "productos": [
            {"sku": "MON-001", "nombre": "Brazo articulado para monitor", "cantidad": 2, "precio": 44.50}
        ],
        "total": 89.00,
        "metodo_pago": "paypal",
        "direccion_envio": {"ciudad": "Valladolid", "codigo_postal": "47001"},
        "notas": None
    },
    {
        "id": 1012,
        "cliente": {"id": 12, "nombre": "Lucía Herrera", "email": "lucia@example.com"},
        "estado": "entregado",
        "fecha": "2026-10-12",
        "productos": [
            {"sku": "ACC-004", "nombre": "Cargador rápido 65W", "cantidad": 1, "precio": 42.00}
        ],
        "total": 42.00,
        "metodo_pago": "bizum",
        "direccion_envio": {"ciudad": "Santander", "codigo_postal": "39001"},
        "notas": None
    },
    {
        "id": 1013,
        "cliente": {"id": 13, "nombre": "Pablo Ortega", "email": "pablo@example.com"},
        "estado": "enviado",
        "fecha": "2026-10-13",
        "productos": [
            {"sku": "INF-005", "nombre": "Disco duro externo 2TB", "cantidad": 1, "precio": 94.90}
        ],
        "total": 94.90,
        "metodo_pago": "tarjeta",
        "direccion_envio": {"ciudad": "Granada", "codigo_postal": "18001"},
        "notas": None
    },
    {
        "id": 1014,
        "cliente": {"id": 14, "nombre": "Nuria Vidal", "email": "nuria@example.com"},
        "estado": "pendiente",
        "fecha": "2026-10-14",
        "productos": [
            {"sku": "AUD-003", "nombre": "Micrófono USB", "cantidad": 1, "precio": 69.90}
        ],
        "total": 69.90,
        "metodo_pago": "transferencia",
        "direccion_envio": {"ciudad": "Lleida", "codigo_postal": "25001"},
        "notas": None
    },
    {
        "id": 1015,
        "cliente": {"id": 15, "nombre": "Óscar Molina", "email": "oscar@example.com"},
        "estado": "cancelado",
        "fecha": "2026-10-15",
        "productos": [
            {"sku": "INF-006", "nombre": "Tarjeta gráfica", "cantidad": 1, "precio": 449.00}
        ],
        "total": 449.00,
        "metodo_pago": "tarjeta",
        "direccion_envio": {"ciudad": "Murcia", "codigo_postal": "30001"},
        "notas": "Cancelado antes del envío"
    },

    # DATOS INCORRECTOS INTENCIONADAMENTE
    {
        "id": 1016,
        "cliente": {"id": 16, "nombre": "Irene Blanco", "email": "irene@example.com"},
        "estado": "pendiente",
        "fecha": "2026-10-16",
        "productos": [
            {"sku": "TEC-005", "nombre": "Teclado compacto", "cantidad": 1, "precio": 59.90}
        ],
        "total": "59.90",  # Importe guardado como string
        "metodo_pago": "tarjeta",
        "direccion_envio": {"ciudad": "Barcelona", "codigo_postal": "08020"},
        "notas": None
    },
    {
        "id": 1017,
        "cliente": {"id": 17, "nombre": "Adrián Pérez", "email": "adrian@example.com"},
        "estado": "pendiente",
        "fecha": "2026-10-16",
        "productos": [
            {"sku": "ACC-005", "nombre": "Cable HDMI", "cantidad": 2, "precio": 14.50}
        ],
        "total": None,  # Importe no informado
        "metodo_pago": "paypal",
        "direccion_envio": {"ciudad": "Badalona", "codigo_postal": "08911"},
        "notas": None
    },
    {
        "id": 1018,
        "cliente": {"id": 18, "nombre": "Claudia Martín", "email": "claudia@example.com"},
        "estado": "pendiente",
        "fecha": "2026-10-16",
        "productos": [
            {"sku": "AUD-004", "nombre": "Auriculares gaming", "cantidad": 1, "precio": 79.90}
        ],
        "total": "incorrecto",  # No se puede convertir a número
        "metodo_pago": "bizum",
        "direccion_envio": {"ciudad": "Gavà", "codigo_postal": "08850"},
        "notas": None
    },
    {
        "id": 1019,
        "cliente": {"id": 19, "nombre": "Víctor García", "email": "victor@example.com"},
        "estado": "desconocido",  # Estado no contemplado
        "fecha": "2026-10-16",
        "productos": [
            {"sku": "INF-007", "nombre": "Procesador Ryzen 7", "cantidad": 1, "precio": 319.00}
        ],
        "total": 319.00,
        "metodo_pago": "tarjeta",
        "direccion_envio": {"ciudad": "Terrassa", "codigo_postal": "08221"},
        "notas": None
    },
    {
        "id": 1020,
        "cliente": {"id": 20, "nombre": "Sara Jiménez", "email": "sara@example.com"},
        "estado": "pendiente",
        "fecha": "2026-10-16",
        "productos": [],
        "total": 0,
        "metodo_pago": "transferencia",
        "direccion_envio": {"ciudad": "Sabadell", "codigo_postal": "08201"},
        "notas": "Pedido sin productos"
    }
]