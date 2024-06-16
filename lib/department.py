from __init__ import CURSOR, CONN


class Department:
    
    all = []

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location
        Department.all.append(self)
        
    @classmethod
    def create_table(cls):
        """Create a new database table to persist attributes from new Department instances"""
        sql = 'CREATE TABLE IF NOT EXISTS departments (id INTEGER PRIMARY KEY, name TEXT, location TEXT)'
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        """Drop from database the departments table that persists department instances"""
        sql = 'DROP TABLE IF EXISTS departments'
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create(cls, name, location):
        """Creates, saves, and returns new class instance"""
        department = cls(name, location)
        department.save()
        return department

    def save(self):
        """Save department instances to database"""
        sql = 'INSERT INTO departments (name, location) VALUES (? , ?)'
        CURSOR.execute(sql, (self.name, self.location))
        # CONN.commit()
        self.id = CURSOR.lastrowid
        
    def update(self):
        sql = """
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()
        
    def delete(self):
        sql = """
            DELETE FROM departments
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

