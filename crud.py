import secrets
import string
from sqlalchemy.orm import Session
import models , schemas, crud


def create_short_url(db: Session, original_url: str):
    # تولید short_code تصادفی
    characters = string.ascii_letters + string.digits
    short_code = ''.join(secrets.choice(characters) for _ in range(6))

    # ذخیره در دیتابیس
    db_url = models.URL(original_url=original_url, short_code=short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url_by_short_code(db: Session, short_code: str):
    return db.query(models.URL).filter(models.URL.short_code == short_code).first()