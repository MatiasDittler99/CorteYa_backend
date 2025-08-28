from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List
from app.core.base_de_datos import get_session
from app.models.modelo_cliente import Cliente
from app.schemas.esquema_cliente import ClienteRead

router = APIRouter(prefix="/clientes-con-turnos", tags=["Clientes con Turnos"])

@router.get("/", response_model=List[ClienteRead])
def listar_clientes_con_turnos(db: Session = Depends(get_session)):
    clientes = session.exec(select(Cliente)).all()
    # SQLModel carga relaciones lazy, entonces accedemos a cliente.turnos para cargarlas
    for cliente in clientes:
        cliente.turnos  # Esto fuerza la carga de turnos
    return clientes
