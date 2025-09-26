from Package.connection import get_connection
from database import taches
from sqlalchemy import select,insert,update,delete
engine=get_connection()

def create_task(contenu, priorite, status):
    with engine.begin() as conn:  
        stmt = insert(taches).values(contenu=contenu, priorite=priorite, status=status)
        conn.execute(stmt)

def get_all_tasks():
    with engine.connect() as conn:
        stmt = select(taches)
        result = conn.execute(stmt)
        return result.fetchall()

def update_task(task_id, contenu, priorite, status):
    with engine.begin() as conn:
        stmt = (
            update(taches)
            .where(taches.c.id == task_id)
            .values(contenu=contenu, priorite=priorite, status=status)
        )
        conn.execute(stmt)


def delete_task(task_id):
    with engine.begin() as conn:
        stmt = delete(taches).where(taches.c.id == task_id)
        conn.execute(stmt)
