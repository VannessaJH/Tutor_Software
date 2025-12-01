
from datetime import datetime
from sqlalchemy.orm import Session
from models.academic.content import Content
from config.database import SessionLocal 
class AdminService:
    
    def get_db(self):
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def get_content_by_slug(self, db: Session, slug: str):
        """Busca una pieza de contenido por su slug."""
        return db.query(Content).filter(Content.slug == slug).first()

    def save_or_update_content(self, data: dict):
        """Guarda o actualiza una pieza de contenido en la BD."""
        
        db = next(self.get_db())
        
        slug = data.get('slug')
        
        if not slug:
            return {"message": "El campo 'slug' es requerido."}, 400
            
        try:
            existing_content = self.get_content_by_slug(db, slug)
            
            if existing_content:
                for key, value in data.items():
                    if hasattr(existing_content, key):
                        setattr(existing_content, key, value)
                
                db.commit()
                db.refresh(existing_content)
                return {"message": f"Contenido '{slug}' actualizado.", "data": existing_content.to_dict()}, 200
            else:
                new_content = Content(
                    title=data.get('title'),
                    slug=slug,
                    content_html=data.get('content_html'),
                    type=data.get('type')
                )
                db.add(new_content)
                db.commit()
                db.refresh(new_content)
                return {"message": f"Contenido '{slug}' creado exitosamente.", "data": new_content.to_dict()}, 201

        except Exception as e:
            db.rollback()
            print(f"Error al guardar/actualizar contenido: {e}")
            return {"message": "Error interno del servidor al guardar contenido."}, 500
        finally:
            db.close()