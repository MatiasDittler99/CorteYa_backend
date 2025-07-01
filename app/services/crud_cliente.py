from typing import List, Optional
from sqlmodel import Session, select
from app.models.modelo_cliente import Cliente
from app.schemas.esquema_cliente import ClienteCreate

def get_clientes(db: Session) -> List[Cliente]:
    return db.exec(select(Cliente)).all()

def get_cliente(db: Session, cliente_id: int) -> Optional[Cliente]:
    return db.get(Cliente, cliente_id)

def create_cliente(db: Session, cliente: ClienteCreate) -> Cliente:
    db_cliente = Cliente.from_orm(cliente)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def update_cliente(db: Session, cliente_id: int, cliente_data: ClienteCreate) -> Optional[Cliente]:
    db_cliente = db.get(Cliente, cliente_id)
    if not db_cliente:
        return None
    for key, value in cliente_data.dict().items():
        setattr(db_cliente, key, value)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def delete_cliente(db: Session, cliente_id: int) -> bool:
    db_cliente = db.get(Cliente, cliente_id)
    if not db_cliente:
        return False
    db.delete(db_cliente)
    db.commit()
    return True
