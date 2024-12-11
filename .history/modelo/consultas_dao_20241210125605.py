from .connecciondb import Conneccion

def crear_tabla():
    conn = Conneccion() # crear coneccion con db
    
    sql1='''
        CREATE TABLE IF NOT EXISTS Genero(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(50),
        PRIMARY KEY (ID AUTOINCREMENT)
        );
        '''
    sql2='''
        CREATE TABLE IF NOT EXISTS Peliculas(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(150),
        Duracion VARCHAR(4),        
        Genero INTEGER,
        Protagonista VARCHAR(150),
        Director VARCHAR(150),
        PRIMARY KEY (ID AUTOINCREMENT)
        FOREIGN KEY (Genero) REFERENCES Genero(ID)
        );
        '''
    sql2='''
        CREATE TABLE IF NOT EXISTS Lugares_de_estreno(
        ID INTEGER NOT NULL,
        Pais VARCHAR(150),               
        Pelicula INTEGER,
        PRIMARY KEY (ID AUTOINCREMENT)
        FOREIGN KEY (Pelicula) REFERENCES Peliculas(ID)
        );
        '''
    sql2='''
        CREATE TABLE IF NOT EXISTS Lugares_de_estreno(
        ID INTEGER NOT NULL,
        Pais VARCHAR(150),               
        Pelicula INTEGER,
        PRIMARY KEY (ID AUTOINCREMENT)
        FOREIGN KEY (Pelicula) REFERENCES Peliculas(ID)
        );
        '''
    try:        
        conn.cursor.execute(sql1)
        conn.cursor.execute(sql2)
        conn.cerrar_con()
    except:
        pass
    #finally:
    #   conn.cerrar_con()

class Peliculas():

    def __init__(self,nombre,duracion,genero,protagonista,director):
        self.nombre = nombre
        self.duracion = duracion
        self.protagonista = protagonista
        self.genero = genero
        self.director = director
        
    
    def __str__(self):
        return f'Pelicula[{self.nombre},{self.duracion},{self.genero},{self.protagonista},{self.director}]'

def guardar_peli(pelicula):
    conn = Conneccion() # crear coneccion con db
    sql=f'''
        INSERT INTO Peliculas (Nombre,Duracion,Genero,Protagonista,Director)
        VALUES('{pelicula.nombre}','{pelicula.duracion}',{pelicula.genero},'{pelicula.protagonista}','{pelicula.director}');
    '''
    try:        
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass
def listar_peli():
    conn = Conneccion() # crear coneccion con db
    listar_peliculas = []

    sql=f'''
        SELECT * FROM Peliculas as p
        INNER JOIN Genero as g
        ON p.Genero = g.ID;
    '''
    try:        
        conn.cursor.execute(sql)
        listar_peliculas = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_peliculas
    except:
        pass

def listar_generos():
    conn = Conneccion() # crear coneccion con db
    listar_genero = []

    sql=f'''
        SELECT * FROM  Genero;
    '''
    try:        
        conn.cursor.execute(sql)
        listar_genero = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_genero
    except:
        pass

def editar_peli(pelicula, id):
    conn = Conneccion() # crear coneccion con db
    sql=f'''
        UPDATE Peliculas
        SET Nombre = '{pelicula.nombre}', Duracion = '{pelicula.duracion}',Genero = {pelicula.genero}, Protagonista = '{pelicula.protagonista}', Director = '{pelicula.director}'
        WHERE ID = {id}
        ;
    '''
    try:        
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass

def borrar_peli(id):
    conn = Conneccion() # crear coneccion con db
    sql=f'''
        DELETE FROM Peliculas        
        WHERE ID = {id}
        ;
    '''
    try:        
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass