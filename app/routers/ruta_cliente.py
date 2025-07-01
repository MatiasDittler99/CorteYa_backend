from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List

from app.schemas.esquema_cliente import ClienteCreate, ClienteRead
from app.services import crud_cliente
from app.core.base_de_datos import get_session

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/", response_model=List[ClienteRead])
def listar_clientes(db: Session = Depends(get_session)):
    return crud_cliente.get_clientes(db)

@router.get("/{cliente_id}", response_model=ClienteRead)
def obtener_cliente(cliente_id: int, db: Session = Depends(get_session)):
    cliente = crud_cliente.get_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.post("/", response_model=ClienteRead)
def crear_cliente(cliente: ClienteCreate, db: Session = Depends(get_session)):
    return crud_cliente.create_cliente(db, cliente)

@router.put("/{cliente_id}", response_model=ClienteRead)
def actualizar_cliente(cliente_id: int, cliente: ClienteCreate, db: Session = Depends(get_session)):
    actualizado = crud_cliente.update_cliente(db, cliente_id, cliente)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return actualizado

@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: int, db: Session = Depends(get_session)):
    eliminado = crud_cliente.delete_cliente(db, cliente_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {"ok": True}
